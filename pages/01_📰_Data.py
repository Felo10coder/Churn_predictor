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

st.write("*The dataset for this project was obtained from an SQL database.Below is a sample of the dataset used for this project*")

## create a connection to a database
@st.cache_resource(show_spinner="connecting to database...")
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

@st.cache_data(show_spinner="Running query...")
def running_query(query):
    with conn.cursor() as cursor:
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

# Create select box at the top
option = st.selectbox(
    "Select data to display",
    ("All Data", "Categorical Columns", "Numerical Columns")
)

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

# Add a file uploader (Dropbox)
uploaded_file = st.file_uploader("Upload a file", type=['csv', 'txt'])
# Check if a file was uploaded
if uploaded_file is not None:
    # Process the uploaded file
    file_contents = uploaded_file.getvalue()
    st.write("Uploaded file contents:")
    st.write(file_contents)



