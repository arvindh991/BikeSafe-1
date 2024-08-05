import osmnx
import networkx as nx
from networkx.classes.multidigraph import MultiDiGraph

from typing import Tuple, List

def get_location_from_address(address: str) -> Tuple[float, float]:
    """ 
    Get (lat, long) coordinates from address
    Args:
        address: string with address
    Returns:
        location: (lat, long) coordinates
    
    From https://stackoverflow.com/questions/58069714/how-to-get-latitude-and-longitude-from-address-using-python
    """
    from geopy.geocoders import Nominatim

    locator = Nominatim(user_agent="myapp")
    location = locator.geocode(address)

    if location:
        return location.latitude, location.longitude
    else:
        return None

def get_graph(address_orig: str, address_dest: str) -> Tuple[MultiDiGraph, Tuple[float, float], Tuple[float, float]]:
    """ 
    Convert the origin and destination addresses into (lat, long) coordinates and find the 
    graph of streets from the bounding box.
    Args:
        address_orig: departure address
        address_dest: arrival address
    Returns:
        graph: street graph from OpenStreetMap
        location_orig: departure coordinates
        location_dest: arrival coordinates
    """

    MARGIN = 0.1

    # find location by address
    location_orig = get_location_from_address(address_orig)
    location_dest = get_location_from_address(address_dest)

    if location_orig is None or location_dest is None:
        return None, None, None

    north = max(location_orig[0], location_dest[0]) + MARGIN
    south = min(location_orig[0], location_dest[0]) - MARGIN
    west = max(location_orig[1], location_dest[1]) + MARGIN
    east = min(location_orig[1], location_dest[1]) - MARGIN

    graph = osmnx.graph.graph_from_bbox(bbox=(north, south, east, west), network_type='bike', clean_periphery=False)
    return graph, location_orig, location_dest

def get_graph_from_mode(address_orig: str, address_dest: str, mode: str, city: str="Melbourne, Australia", dist: float=1000.0) -> Tuple[MultiDiGraph, Tuple[float, float], Tuple[float, float]]:
    """
    Convert the origin and destination addresses into (lat, long) coordinates and find the
    graph of streets from the bounding box.
    Args:
        address_orig: departure address
        address_dest: arrival address
        mode: get graph from place or from address
        city: name of the city/town
        dist: distance from the original address in meters
    Returns:
        graph: street graph from OpenStreetMap
        location_orig: departure coordinates
        location_dest: arrival coordinates
    """

    assert mode in ['place', 'address']

    # find location by address
    location_orig = get_location_from_address(address_orig)
    location_dest = get_location_from_address(address_dest)

    if location_orig is None or location_dest is None:
        return None, None, None

    if mode == 'place':
        graph = osmnx.graph_from_place(city, network_type='bike')
    else:
        graph = osmnx.graph.graph_from_address(address_orig, dist=dist, dist_type='bbox', network_type='bike')

    return graph, location_orig, location_dest

def find_shortest_path(graph: MultiDiGraph, location_orig: Tuple[float, float], location_dest: Tuple[float, float]) -> List[int]:
    """
    Find the shortest path between two points from the street graph
    Args:
        graph: street graph from OpenStreetMap
        location_orig: departure coordinates
        location_dest: arrival coordinates
        optimizer: type of optimizer (Length or Time)
    Returns:
        route: list of nodes representing the shortest path
    """

    ## find the nearest node to the departure and arrival location
    #node_orig = osmnx.get_nearest_node(graph, location_orig)
    #node_dest = osmnx.get_nearest_node(graph, location_dest)
    orig = osmnx.distance.nearest_nodes(graph, location_orig[1], location_orig[0])
    dest = osmnx.distance.nearest_nodes(graph, location_dest[1], location_dest[0])

    route = osmnx.shortest_path(graph, orig, dest, weight='travel_time')
    return route
