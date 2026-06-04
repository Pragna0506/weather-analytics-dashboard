import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title("🧠 Weather Insights")

df = pd.read_parquet("data/weather.2016.parquet")

st.write(df.describe())

numeric = df.select_dtypes(include="number")

corr = numeric.corr()

st.subheader("Correlation Matrix")

st.dataframe(corr)

highest = corr.unstack().sort_values(
    ascending=False
)

st.success(
    "Strongest Weather Relationships Identified"
)
