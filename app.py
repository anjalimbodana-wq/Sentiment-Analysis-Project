import streamlit as st
import pandas as pd

st.title("Sentiment Analysis Dashboard")

df = pd.read_csv("output.csv")

st.write(df)

st.bar_chart(df["Sentiment"].value_counts())