# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.title("🌍 Geo Analytics")

# cities = pd.read_csv("data/cities.csv")
# countries = pd.read_csv("data/countries.csv")

# st.dataframe(cities.head())

# fig = px.scatter_geo(
#     cities,
#     lat="latitude",
#     lon="longitude",
#     hover_name="city"
# )

# st.plotly_chart(fig, use_container_width=True)
import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Geo Analytics",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Geo Analytics Dashboard")
st.markdown("Explore weather stations and cities across the globe.")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    cities = pd.read_csv("data/cities.csv")
    countries = pd.read_csv("data/countries.csv")
    return cities, countries

cities, countries = load_data()

# --------------------------------------------------
# DATA PREVIEW
# --------------------------------------------------

with st.expander("📄 Cities Dataset Preview"):
    st.dataframe(cities.head(), use_container_width=True)

# --------------------------------------------------
# SUMMARY KPIs
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Cities", f"{len(cities):,}")

with col2:
    st.metric("Countries", cities["country"].nunique())

with col3:
    st.metric("Weather Stations", cities["station_id"].nunique())

# --------------------------------------------------
# COUNTRY FILTER
# --------------------------------------------------

countries_list = sorted(cities["country"].dropna().unique())

selected_country = st.selectbox(
    "Select Country",
    ["All Countries"] + countries_list
)

if selected_country != "All Countries":
    filtered_df = cities[
        cities["country"] == selected_country
    ]
else:
    filtered_df = cities.copy()

# --------------------------------------------------
# GEO MAP
# --------------------------------------------------

st.subheader("🗺️ Global Weather Station Map")

fig = px.scatter_geo(
    filtered_df,
    lat="latitude",
    lon="longitude",
    hover_name="city_name",
    hover_data={
        "country": True,
        "state": True,
        "iso2": True,
        "latitude": False,
        "longitude": False
    },
    title="Weather Stations Worldwide"
)

fig.update_layout(
    height=700,
    geo=dict(
        showland=True,
        showcountries=True
    ),
    margin=dict(
        l=0,
        r=0,
        t=50,
        b=0
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# COUNTRY DISTRIBUTION
# --------------------------------------------------

st.subheader("📊 Top Countries by Number of Cities")

country_count = (
    filtered_df["country"]
    .value_counts()
    .head(15)
    .reset_index()
)

country_count.columns = [
    "Country",
    "Cities"
]

fig2 = px.bar(
    country_count,
    x="Country",
    y="Cities",
    title="Top 15 Countries"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# --------------------------------------------------
# CITY TABLE
# --------------------------------------------------

st.subheader("🏙️ City Details")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# --------------------------------------------------
# DOWNLOAD
# --------------------------------------------------

csv = filtered_df.to_csv(index=False)

st.download_button(
    "⬇️ Download Filtered Data",
    csv,
    "cities_data.csv",
    "text/csv"
)
