import streamlit as st
import pyodbc
import pandas as pd
import os
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title = "Data page",
    page_icon = "🗃️",
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

    st.title('CUSTOMER CHURN DATABASE')
    st.sidebar.success("select a page above")

    st.write("""*Welcome to the Customer Churn Data Analysis page!
         Here, you'll find detailed insights into customer behavior and churn patterns.This dataset, retrieved directly from our SQL database, 
         offers a comprehensive look at various factors influencing customer retention and attrition.
         Explore the data to uncover trends, identify key metrics, 
         and gain a deeper understanding of what drives customer churn in our business.*""")

## create a connection to a database

    st.cache_resource(show_spinner="connecting to database...")
    def init_connection():
        connection_string = (
        "DRIVER={SQL Server};"
        "SERVER=" + st.secrets['server'] + ";"
        "DATABASE=" + st.secrets['database'] + ";"
        "UID=" + st.secrets['user'] + ";"
        "PWD=" + st.secrets['password']
    )
        return pyodbc.connect(connection_string)
    
    conn = init_connection()

    st.cache_data(show_spinner="Running query...")
    def running_query(query):
        with conn.cursor()as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            df = pd.DataFrame.from_records(rows, columns=columns)
        return df


    def get_all_columns():
        sql_query = "SELECT * FROM dbo.LP2_Telco_churn_first_3000"
        df = running_query(sql_query)
        return df

# Load data
    df = get_all_columns()

# Identify categorical and numerical columns
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
    numerical_columns = df.select_dtypes(include=['number']).columns.tolist()

    col1,col2=st.columns(2)
    with col1:
    # Create select box at the top
        option = st.selectbox(
    "Select data to display",
    ("All Data", "Categorical Columns", "Numerical Columns")
    )
    with col2:
        pass    

# Display data based on selection
    if option == "All Data":
        st.write(df)
    elif option == "Categorical Columns":
        st.write(df[categorical_columns])
    elif option == "Numerical Columns":
        st.write(df[numerical_columns])    
# Add a description with the embedded link
    st.write("To get a brief definition of each column in the data set, please [Go to Data Dictionary Page](http://localhost:8501/data_dictionary).")
    st.write("Users can upload their own data using the below drag and drop option. However, the data has to have the same features as the above dataset ")
    col1,col2=st.columns(2)
    with col1:
# Add a file uploader (Dropbox)
        uploaded_file = st.file_uploader("Upload a file", type=['csv', 'txt'])
# Check if a file was uploaded
        if uploaded_file is not None:
    # Process the uploaded file
            file_contents = uploaded_file.getvalue()
            st.write("Uploaded file contents:")
            st.write(file_contents)
    with col2:
        pass
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.info('Log in to access the page')
    st.code("""
            usernames:felixkwemoi
            password: FKM#101""")

