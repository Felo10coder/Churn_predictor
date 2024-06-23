import streamlit as st
import pandas as pd
import os
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title = "History page",
    page_icon = "📜",
    layout = 'wide'
)
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login(location='sidebar') ## to show the log in form

if st.session_state["authentication_status"]:
    authenticator.logout(location='sidebar')
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
      
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.info('Log in to access the page')
    st.code("""
            usernames:felixkwemoi
            password: FKM#101""")     