import json
import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime, timedelta
from streamlit_date_picker import date_range_picker, PickerType

st.title("Melbourne Traffic Accidents")

map_json = "data/melbourne.geojson"
regions_geojson = json.load(open(map_json))

accidents_data = pd.read_parquet("data/accidents_data.parquet")
accidents_data_extract = accidents_data.copy()
default_start, default_end = datetime.strptime('2012-01-01', "%Y-%m-%d"), datetime.now()
date_range_string = date_range_picker(picker_type=PickerType.date,
                                      start=default_start, end=default_end,
                                      key='date_range_picker',
                                      )
if date_range_string:
    start, end = date_range_string
    st.write(f"Date Range Picker [{start}, {end}]")

    #convert start to date
    start_date = pd.Timestamp(datetime.strptime(start, "%Y-%m-%d").date())
    end_date = pd.Timestamp(datetime.strptime(end, "%Y-%m-%d").date())
    accidents_data_extract = accidents_data[(accidents_data["ACCIDENT_DATE"] >= start_date) & (accidents_data["ACCIDENT_DATE"] < end_date)]


accidents_count = accidents_data_extract.groupby("name").size().reset_index(name="accidents_count")
accidents_count.sort_values("accidents_count", ascending=False, inplace=True)

fig = px.choropleth(
    data_frame = accidents_count,
    geojson=regions_geojson,
    locations="name",
    featureidkey="properties.name",
    color="accidents_count",
)
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

event = st.plotly_chart(fig, theme=None, on_select="rerun", selection_mode="points")

try: 
    region_selected = event["selection"]["points"][0]["location"] if event else None
except IndexError:
    region_selected = None

if region_selected:
    accidents_data_region = accidents_data_extract[accidents_data_extract["name"] == region_selected]

    causes = accidents_data_region["CAUSE"].value_counts()
    cause_list = causes.index.tolist()
    causes_selected = st.multiselect("Select causes", cause_list, default=cause_list)
    accidents_data_region_causes = accidents_data_region[accidents_data_region["CAUSE"].isin(causes_selected)]
    accidents_data_region_severity = accidents_data_region_causes["SEVERITY"].value_counts().reset_index(name="Counts")
    fig_severity = px.bar(accidents_data_region_severity, x="SEVERITY", y="Counts")
    st.plotly_chart(fig_severity, theme=None)