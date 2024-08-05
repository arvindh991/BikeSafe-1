import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="BikeSafe Melbourne", page_icon="🚲", layout="wide")

# Custom CSS to style the page and buttons
st.markdown("""
<style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1541625602330-2277a4c46182?q=80&w=1740&auto=format&fit=crop');
        background-size: cover;
    }
    .main-header, .sub-header {
        color: white;
        font-weight: bold;
        text-align: center;
        padding: 2rem 0;
        background-color: rgba(0, 0, 0, 0.5);
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
        font-family: 'Arial Black', Gadget, sans-serif;
    }
    .main-header {
        font-size: 3.5rem;
    }
    .sub-header {
        font-size: 1.5rem;
    }
    .stat-box {
        background-color: #F0F0F0;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem;
        cursor: pointer;
    }
    .center-text {
        text-align: center;
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 20px;
    }
    .button {
        background-color: #F0F0F0;
        border: 2px solid #CCCCCC;
        color: #333333;
        padding: 15px 32px;
        text-align: left;
        text-decoration: none;
        display: flex;
        align-items: center;
        font-size: 18px;
        cursor: pointer;
        border-radius: 30px;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        font-family: 'Arial Black', Gadget, sans-serif;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        width: 300px;
    }
    .button:hover {
        background-color: #E0E0E0;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    .button-icon {
        background-color: #007BFF;
        color: white;
        border-radius: 50%;
        padding: 10px;
        margin-right: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 50px;
        height: 50px;
    }
    .hidden-content {
        display: none;
        background-color: rgba(255, 255, 255, 0.9);
        padding: 1rem;
        border-radius: 10px;
        margin-top: 0.5rem;
    }
    .stat-box:hover + .hidden-content {
        display: block;
    }
</style>
""", unsafe_allow_html=True)

# Navigation bar
col1, col2, col3, col4, col5 = st.columns([2,1,1,1,1])
with col1:
    st.image("https://placeholder.com/wp-content/uploads/2018/10/placeholder.com-logo1.png", width=150)

# Main header
st.markdown("<h1 class='main-header'>Less Waste, Less Waist, Go Safe</h1>", unsafe_allow_html=True)

# Statistics at the top with expandable content
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class='stat-box center-text'><h3>500+</h3>Accident Reports</div>
    <div class='hidden-content'>
        <p>Cycling deaths are slowly declining in Australia, but fatalities involving single riders and older people are on the rise.

Analysis of the 1294 cyclist fatalities recorded in Australia over the last three decades shows cycling deaths slightly decreased overall by an average of 1.1 per cent annually. However, fatalities in those aged 60 years and over increased by 3.3 per cent annually over the same period. .</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class='stat-box center-text'><h3>200 km</h3>Safe Bike Lanes</div>
    <div class='hidden-content'>
        <p>By choosing biking as your main transportation method, you not only contribute to reducing pollution but you’re also helping improve the air quality in your neighborhood. Moreover, many researchers have studied the relationship between exercise and cancer, especially colon and breast cancer. Research has shown that if you cycle, the chance of bowel cancer is reduced. Some evidence suggests that regular cycling reduces the risk of breast cancer.
        .</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class='stat-box center-text'><h3>50+</h3>Community Routes</div>
    <div class='hidden-content'>
        <p>The City of Melbourne’s cycling network has over 135 km of on and off road routes.
        Melbourne boasts over 200 km of dedicated bike lanes, providing safe routes for cyclists throughout the city.</p>
    </div></p>
    </div>
    """, unsafe_allow_html=True)

# Welcome message
st.markdown("<div class='sub-header'><strong>Welcome!</strong> BikeSafe Melbourne is your ultimate companion for cycling through the vibrant streets and welcoming architecture.</div>", unsafe_allow_html=True)

# Centered buttons with links
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("""
    <div class='button-container'>
        <a href='https://bikesafe.streamlit.app/Safe_Bike_Lanes' target='_blank' class='button'>
            <div class='button-icon'>🚴🏼‍♂️</div> Discover Routes
        </a>
        <a href='https://bikesafe.streamlit.app/Accident_Statistics' target='_blank' class='button'>
            <div class='button-icon'>📊</div> Accident Statistics
        </a>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<div class='center-text' style='position: fixed; bottom: 0; width: 100%; background-color: rgba(255,255,255,0.8); padding: 10px;'>© 2024 BikeSafe Melbourne. Ride smart, ride safe!</div>", unsafe_allow_html=True)
