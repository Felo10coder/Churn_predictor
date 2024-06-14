import streamlit as st
import pyodbc
import pandas as pd

st.set_page_config(
    page_title = "Data page",
    page_icon = "🗃️",
    layout = 'wide'
)
st.title('CUSTOMER CHURN DATABASE')
st.sidebar.success("select a page above")

