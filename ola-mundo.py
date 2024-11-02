import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")


df_rewiews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")



df_rewiews