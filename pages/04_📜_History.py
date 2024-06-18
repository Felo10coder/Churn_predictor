import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title = "History page",
    page_icon = "📜",
    layout = 'wide'
)
st.title('CUSTOMER CHURN HISTORY DATA')
st.sidebar.success("select a page above")

def display_historic_data():
    csv_path='./data/history_data.csv'
    csv_exists=os.path.exists(csv_path)
    if csv_exists:
        historic_data=pd.read_csv(csv_path) 
    return st.dataframe(historic_data)
        

if __name__ == '__main__':
    display_historic_data()        