import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Geo Analytics")

cities = pd.read_csv("data/cities.csv")
countries = pd.read_csv("data/countries.csv")

st.dataframe(cities.head())

fig = px.scatter_geo(
    cities,
    lat="latitude",
    lon="longitude",
    hover_name="city"
)

st.plotly_chart(fig, use_container_width=True)
