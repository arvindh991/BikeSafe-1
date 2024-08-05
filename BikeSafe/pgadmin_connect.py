import streamlit as st
import psycopg2
import pandas as pd

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

# Your specific query
query = """
SELECT 
    v.ACCIDENT_NO,
    v.VEHICLE_TYPE,
    a.ACCIDENT_DATE,
    a.ACCIDENT_TIME,
    a.node_id,
    a.ACCIDENT_TYPE
FROM 
    vehicle v
JOIN 
    accident a ON v.ACCIDENT_NO = a.ACCIDENT_NO
WHERE 
    v.VEHICLE_TYPE = '13';
"""

# Run the query and fetch the results
rows = run_query(query)

# Convert the results to a DataFrame
data = pd.DataFrame(rows, columns=['ACCIDENT_NO', 'VEHICLE_TYPE', 'ACCIDENT_DATE', 'ACCIDENT_TIME', 'NODE_ID', 'ACCIDENT_TYPE'])

# Display the data in Streamlit
st.title('Accident Data for Vehicle Type 13')
st.dataframe(data)

# You can add more Streamlit components to interact with or visualize the data
st.write(f"Total number of accidents: {len(data)}")

# Example: Histogram of accidents by date
st.subheader('Accidents by Date')
st.bar_chart(data['ACCIDENT_DATE'].value_counts())

# Example: Pie chart of accident types
st.subheader('Distribution of Accident Types')
st.pie_chart(data['ACCIDENT_TYPE'].value_counts())