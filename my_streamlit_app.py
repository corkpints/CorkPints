
import streamlit as st
import pandas as pd
import folium

from streamlit_folium import st_folium

 # Custom CSS for styling
custom_css = """
    <style>
        body {
            background-color: #f0f2f6;
            color: #333333;
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
        }
        h1 {
            color: #007bff;
            text-align: center;
            margin-bottom: 30px;
        }
        .leaflet-container {
            height: 500px;
            width: 100%;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

st.title('Cork Pubs Map')

# Load data
pubs_df = pd.read_csv("cork_pubs.csv")

# Create the map
mymap = folium.Map(location=[51.89598936975075, -8.487619607745506], zoom_start=15.3)

# Add markers to the map
for index, row in pubs_df.iterrows():
    if not pd.isna(row['completed']):
        color = 'green'
    else:
        color = 'red'
    folium.Marker(location=[row['lat'], row['lon']], 
                  popup=row['name'],
                  icon=folium.Icon(color=color)).add_to(mymap)

# Display the map
st_folium(mymap)
