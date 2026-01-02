import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium

df = pd.read_csv("earthquakes_yesterday.csv")

st.set_page_config(layout="wide")

st.title("Earthquake Global Map")
mean_lat = df["Latitude"].mean()
mean_lon = df["Longitude"].mean()

m = folium.Map(location=[mean_lat, mean_lon], zoom_start=2)

for i, row in df.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    loc = {row["Location"]}
    mag = {row["Magnitude"]}
    folium.CircleMarker(
        location=[lat, lon], 
        radius=row["Magnitude"] * 2,
        tooltip=f"Loc{loc} Mag: {mag}"
        ).add_to(m)

st_folium(m, width=1460)