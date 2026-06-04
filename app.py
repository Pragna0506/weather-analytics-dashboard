import streamlit as st

st.set_page_config(
    page_title="Global Weather Analytics",
    page_icon="🌦️",
    layout="wide"
)

st.title("🌦️ Global Weather Analytics Dashboard")

st.markdown("""
### Project Overview

This dashboard provides:

- Global Weather Trends
- Climate Analytics
- Country-wise Insights
- Temperature Analysis
- Rainfall Analysis
- Interactive Visualizations

Use the sidebar to navigate through pages.
""")

st.image(
    "https://images.unsplash.com/photo-1504608524841-42fe6f032b4b",
    use_container_width=True
)

st.success("Dataset Loaded Successfully")
