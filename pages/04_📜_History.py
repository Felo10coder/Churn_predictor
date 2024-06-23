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
st.write("""Welcome to the Prediction History page!
         This section records all user inputs and the corresponding predictions generated on the Prediction page.
         Here, you can review past inputs, track the outcomes, and analyze the predictive performance over time.
         Dive into the history to gain insights and verify the accuracy of our churn prediction models.""")

def display_historic_data():
    csv_path='./data/history_data.csv'
    csv_exists=os.path.exists(csv_path)
    if csv_exists:
        historic_data=pd.read_csv(csv_path) 
    return st.dataframe(historic_data)
        

if __name__ == '__main__':
    display_historic_data()        