import streamlit as st

# Set page configuration
st.set_page_config(page_title="BikeSafe Melbourne", page_icon="🚲", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for styling
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        background-color: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(10px);
    }
    .navbar-brand {
        color: #FFFFFF;
        font-size: 1.5rem;
        font-weight: bold;
    }
    .navbar-links a {
        color: #FFFFFF;
        text-decoration: none;
        margin-left: 1rem;
    }
    .hero-container {
        position: relative;
        height: 100vh;
        width: 100vw;
        overflow: hidden;
        margin-top: -80px;  /* Adjust this value based on your navbar height */
    }
    .hero-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .hero-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
    }
    .hero-title-box {
        background-color: rgba(0, 0, 0, 0.6); /* Semi-transparent box for title */
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .hero-subtitle-box {
        background-color: rgba(0, 0, 0, 0.6); /* Semi-transparent box for subtitle */
        padding: 15px;
        border-radius: 10px;
    }
    .hero-title {
        font-size: 3rem;
        font-weight: bold;
        color: #f2e8cf;
    }
    .hero-subtitle {
        font-size: 1.5rem;
        color: f2e8cf;
    }
    .main-content {
        padding: 2rem;
    }
    .section-title {
        font-size: 2rem;
        font-weight: bold;
        color: #007BFF;
        margin-bottom: 1rem;
    }
    .section-content {
        color: #FFFFFF;
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
    }
    .stButton>button {
        background-color: #007BFF;
        color: #FFFFFF;
    }
</style>
""", unsafe_allow_html=True)

# Navigation bar
st.markdown("""
<div class="navbar">
    <div class="navbar-brand">BikeSafe</div>
    <div class="navbar-links">
        <a href="Safe_Bike_Lanes">Discover Routes</a>
        <a href="Accident_Statistics">Accident Statistics</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="hero-container">
    <img src="https://images.unsplash.com/photo-1541625602330-2277a4c46182?q=80&w=1740&auto=format&fit=crop" class="hero-image" alt="Cyclists riding">
    <div class="hero-text">
        <div class="hero-title-box">
            <h1 class="hero-title">Every Ride Counts. Safety Matters.</h1>
        </div>
        <div class="hero-subtitle-box">
            <p class="hero-subtitle">Discover essential safety insights for cyclists, helping you navigate the roads confidently and securely. Ride smart, stay safe.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# Main content
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Safe bike lanes section
col1, col2 = st.columns(2)
with col1:
    st.image("media/bike tracks.jpeg", use_column_width=True)
with col2:
    st.markdown("<h2 class='section-title'>Discover Safer Bike Lanes</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='section-content'>
        Discover Melbourne's extensive network of safe bike lanes. Our app provides:
        <ul>
            <li>Up-to-date information on dedicated cycling paths</li>
            <li>Shared lanes and low-traffic routes</li>
            <li>Real-time updates on road conditions</li>
            <li>Community-reported hazards and tips</li>
            <li>Integration with traffic signals for safer rides</li>
        </ul>
        Ensure a safe and enjoyable ride every time with BikeSafe Melbourne.
        <a href="Safe_Bike_Lanes"><button>Explore Safe Routes</button></a>
    </div>
    """, unsafe_allow_html=True)
    #st.button("Explore Safe Routes")

# Accident Statistics section
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h2 class='section-title'>Accident Statistics</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='section-content'>
        Stay informed about cycling safety in Melbourne. Our comprehensive statistics include:
        <ul>
            <li>Historical accident data and trends</li>
            <li>Interactive heatmaps of high-risk areas</li>
            <li>Time-based analysis of accident occurrences</li>
            <li>Detailed reports on accident types and causes</li>
            <li>Safety improvement suggestions based on data analysis</li>
        </ul>
        Make informed decisions about your routes and stay safe on the roads with BikeSafe Melbourne.
        <a href="Accident_Statistics"><button>View Statistics</button></a>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("	https://pbs.twimg.com/media/De69pPpUYAAFMrh?format=jpg&name=900x900", use_column_width=True)
col1, col2 = st.columns(2)
with col1:
    st.image("BikeSafe/media/bike tracks.jpeg", use_column_width=True)
with col2:
    st.markdown("<h2 class='section-title'>Discover Safer Bike Lanes</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='section-content'>
        Discover Melbourne's extensive network of safe bike lanes. Our app provides:
        <ul>
            <li>Up-to-date information on dedicated cycling paths</li>
            <li>Shared lanes and low-traffic routes</li>
            <li>Real-time updates on road conditions</li>
            <li>Community-reported hazards and tips</li>
            <li>Integration with traffic signals for safer rides</li>
        </ul>
        Ensure a safe and enjoyable ride every time with BikeSafe Melbourne.
    </div>
    """, unsafe_allow_html=True)
    st.button("Explore Safe Routes")

# Accident Statistics section
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h2 class='section-title'>Accident Statistics</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='section-content'>
        Stay informed about cycling safety in Melbourne. Our comprehensive statistics include:
        <ul>
            <li>Historical accident data and trends</li>
            <li>Interactive heatmaps of high-risk areas</li>
            <li>Time-based analysis of accident occurrences</li>
            <li>Detailed reports on accident types and causes</li>
            <li>Safety improvement suggestions based on data analysis</li>
        </ul>
        Make informed decisions about your routes and stay safe on the roads with BikeSafe Melbourne.
    </div>
    """, unsafe_allow_html=True)
    st.button("View statistics")
with col2:
    st.image("https://pbs.twimg.com/media/De69pPpUYAAFMrh?format=jpg&name=900x900", use_column_width=True)


st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("<div style='text-align: center; color: #FFFFFF; padding: 1rem; margin-top: 2rem;'>© 2024 BikeSafe Melbourne. Ride smart, ride safe!</div>", unsafe_allow_html=True)