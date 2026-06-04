import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dataset Overview")

df = pd.read_parquet("data/daily_weather.parquet")

st.metric("Rows", f"{len(df):,}")
st.metric("Columns", len(df.columns))

st.dataframe(df.head())

st.subheader("Missing Values")

missing = df.isnull().sum().sort_values(ascending=False)

fig = px.bar(
    x=missing.index,
    y=missing.values,
    title="Missing Values"
)

st.plotly_chart(fig, use_container_width=True)
