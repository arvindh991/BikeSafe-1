import json
import osmnx
import folium
import streamlit as st
from streamlit_folium import folium_static

from bikesafe.navigation import (get_location_from_address,
                            get_graph,
                            get_graph_from_mode,
                            find_shortest_path) 

ADDRESS_DEFAULT = "Melbourne, Australia"

def clear_text():
    st.session_state["go_from"] = ""
    st.session_state["go_to"] = ""

with st.sidebar:
    st.title("Choose you travel settings")
    st.markdown("A simple app that finds and displays the shortest path between two points on a map.")
    basemap = 'OpenStreetMap'
    address_from = st.text_input("Go from", key="go_from")
    address_to = st.text_input("Go to", key="go_to")
    st.button("Clear all address boxes", on_click=clear_text)
    st.write(address_to)
    st.info(
        "This is based on "
        "[streamlit-navigator](https://github.com/maxmarkov/streamlit-navigator/issues). "
    )

lat, lon = get_location_from_address(address=ADDRESS_DEFAULT)
st.write(f"Lat, Lon: {lat}, {lon}")
m = folium.Map(location=[lat, lon], zoom_start=12)

def my_style(feature):
    style = {
        "color": "blue",
        "weight": 1,
    }
    return style
bike_route_json = "data/melbourne-bicycle-network-clean.geojson"
bike_routes = json.load(open(bike_route_json))

if address_from and address_to:
    graph, location_orig, location_dest = get_graph(address_from, address_to)
    folium.Marker(location=list(location_orig), icon=folium.Icon(color='red', icon='suitcase', prefix='fa')).add_to(m)
    folium.Marker(location=list(location_dest), icon=folium.Icon(color='green', icon='street-view', prefix='fa')).add_to(m)
    folium.GeoJson(bike_routes, name="Bike Lanes", style_function=my_style, marker=None, show=False).add_to(m)
    folium.LayerControl().add_to(m)
    st.markdown(f'**From**: {address_from}')
    st.markdown(f'**To**: {address_to}')
    route = find_shortest_path(graph, location_orig, location_dest)
    osmnx.plot_route_folium(graph, route, m)
    folium_static(m)

else:
    folium.GeoJson(bike_routes, name="Bike Lanes", style_function=my_style, marker=None).add_to(m)
    folium.LayerControl().add_to(m)
    folium_static(m)
    st.write("Done!")

# Ground Cafe, Melbourne
# Coe & Coe, Melbourne

# Moody Brew, Melbourne
# Thyme Square Cafe, Melbourne