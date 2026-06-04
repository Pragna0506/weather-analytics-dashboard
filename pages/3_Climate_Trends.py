import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Climate Trends")

df = pd.read_parquet("data/daily_weather.parquet")

numeric_cols = df.select_dtypes(include="number").columns

metric = st.selectbox(
    "Select Weather Metric",
    numeric_cols
)

fig = px.line(
    df,
    y=metric,
    title=f"{metric} Trend"
)

st.plotly_chart(fig, use_container_width=True)
