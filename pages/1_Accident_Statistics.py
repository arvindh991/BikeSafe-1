import json
import pandas as pd
import streamlit as st
import plotly.express as px
import folium
from streamlit_folium import st_folium
from datetime import datetime
from branca.colormap import LinearColormap
from shapely.geometry import Point
import geopandas as gpd

st.set_page_config(layout="wide", page_title="Melbourne Traffic Accidents")

# Custom CSS for layout improvements
st.markdown("""
<style>
.reportview-container .main .block-container {
    padding-top: 2rem;
    padding-right: 1rem;
    padding-left: 1rem;
    padding-bottom: 2rem;
}
.stSlider {
    padding-top: 1rem;
    padding-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.title("Melbourne Traffic Accidents")

# Load data
map_json = "data/melbourne.geojson"
regions_geojson = json.load(open(map_json))
regions = gpd.read_file(map_json)
accidents_data = pd.read_parquet("data/accidents_data.parquet")

# Date slider
min_date = accidents_data['ACCIDENT_DATE'].min().date()
max_date = accidents_data['ACCIDENT_DATE'].max().date()
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    start_date, end_date = st.slider(
        "Select date range",
        min_value=min_date,
        max_value=max_date,
        value=(min_date, max_date)
    )

# Filter data based on date range
accidents_data_extract = accidents_data[
    (accidents_data['ACCIDENT_DATE'].dt.date >= start_date) & 
    (accidents_data['ACCIDENT_DATE'].dt.date <= end_date)
]

# Prepare data for choropleth
accidents_count = accidents_data_extract.groupby("name").size().reset_index(name="accidents_count")

# Create base map
m = folium.Map(location=[-37.8136, 144.9631], zoom_start=13)

# Create a colormap
colormap = LinearColormap(colors=['#FED976', '#FEB24C', '#FD8D3C', '#FC4E2A', '#E31A1C', '#BD0026'], 
                          vmin=accidents_count['accidents_count'].min(), 
                          vmax=accidents_count['accidents_count'].max())

# Add choropleth layer
folium.Choropleth(
    geo_data=regions_geojson,
    name='Accidents',
    data=accidents_count,
    columns=['name', 'accidents_count'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Number of Accidents'
).add_to(m)

# Add hover functionality
folium.GeoJson(
    regions_geojson,
    style_function=lambda feature: {
        'fillColor': 'transparent',
        'color': 'black',
        'weight': 2,
        'fillOpacity': 0.7,
    },
    tooltip=folium.GeoJsonTooltip(
        fields=['name'],
        aliases=['Region:'],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
    )
).add_to(m)

# Layout
col1, col2 = st.columns([1, 3])

with col1:
    st.subheader("About This Visualization")
    st.write("""
    This interactive map visualizes traffic accidents in Melbourne, Australia. 
    The color intensity represents the number of accidents in each region, with darker colors indicating a higher number of incidents.
    
    Use the date slider above to filter accidents within a specific time range.
    
    Click on a region to view detailed accident statistics for that area.
    """)
    
    st.subheader("Instructions")
    st.write("""
    1. Adjust the date range using the slider above the map.
    2. Hover over regions to see their names.
    3. Click on a region to view its accident statistics.
    4. Use the zoom controls on the map to focus on specific areas.
    """)
    
    # Placeholder for region-specific information
    st.subheader("Region Statistics")
    region_stats = st.empty()

with col2:
    map_data = st_folium(m, width=1500, height=800)

# Legend
colormap.add_to(m)

# Handle map clicks
clicked_region = None

if map_data['last_clicked'] is not None:
    lat = map_data['last_clicked']['lat']
    long = map_data['last_clicked']['lng']
    d = {'geometry': [Point(long, lat)]}
    gdf = gpd.GeoDataFrame(d, crs="EPSG:4326")
    location = gpd.sjoin(gdf, regions, how="left", predicate="within")
    name = location['name'].values[0]
    if type(name) == str:
        clicked_region = name

if clicked_region:
    accidents_data_region = accidents_data_extract[accidents_data_extract["name"] == clicked_region]
    
    with region_stats.container():
        st.write(f"Selected region: {clicked_region}")
        
        causes = accidents_data_region["CAUSE"].value_counts()
        cause_list = causes.index.tolist()
        causes_selected = st.multiselect("Select causes", cause_list, default=cause_list[:5])
        
        accidents_data_region_causes = accidents_data_region[accidents_data_region["CAUSE"].isin(causes_selected)]
        accidents_data_region_severity = accidents_data_region_causes["SEVERITY"].value_counts().reset_index(name="Counts")
        
        fig_severity = px.bar(accidents_data_region_severity, x="SEVERITY", y="Counts", 
                              title=f"Accident Severity in {clicked_region}",
                              color_discrete_sequence=["#FFA07A"])
        st.plotly_chart(fig_severity, use_container_width=True)
else:
    with region_stats.container():
        st.write("Click on a region to view its accident statistics.")
