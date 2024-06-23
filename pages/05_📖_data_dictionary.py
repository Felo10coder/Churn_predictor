import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title = "Customer Data Dictionary",
    page_icon = "📚",
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
# Title
    st.title("Customer Data Dictionary")
    st.sidebar.success("select a page above")
# Markdown table
    st.write("""Welcome to the Customer Dictionary page! 
         This section provides detailed descriptions of each feature or column in our dataset. 
         Understanding these features is crucial for interpreting the data and the results of our analyses. 
         Use this page as a reference to gain clarity on the attributes that influence
         customer churn and how they are defined in our telecommunication dataset.""")
    st.markdown("""
### Customer Data Dictionary

| Column Name         | Description                                                                      |
|---------------------|----------------------------------------------------------------------------------|
| `customerID`        | Unique identifier of different customers                                         |
| `gender`            | Sex of the customer (male or female)                                             |
| `SeniorCitizen`     | 'No' to show customer is not a SeniorCitizen and 'Yes' to show a SeniorCitizen    |
| `Partner`           | Indicates if the customer has a partner                                          |
| `Dependents`        | Shows if the customer has individuals depending on them                          |
| `tenure`            | The period the customer has been using the company services                      |
| `PhoneService`      | Indicates if the customer has a phone service                                    |
| `MultipleLines`     | Indicates if the customer has multiple lines                                     |
| `InternetService`   | Indicates if the customer has an Internet service                                |
| `OnlineSecurity`    | Indicates if the customer has online security                                    |
| `OnlineBackup`      | Indicates if the customer has online backup                                      |
| `DeviceProtection`  | Indicates if the customer has device protection                                  |
| `TechSupport`       | Indicates if the customer has tech support                                       |
| `StreamingTV`       | Shows if the customer streams their TV                                           |
| `StreamingMovies`   | Shows if the customer streams their movies                                       |
| `Contract`          | Shows the type of contract the customer has                                      |
| `PaperlessBilling`  | Indicates if the customer's billing is done on paper                             |
| `PaymentMethod`     | Shows the method used in buying services                                         |
| `MonthlyCharges`    | Amount paid by the customer on a monthly basis                                   |
| `TotalCharges`      | Amount the customer has paid throughout their tenure using the company services  |
| `Churn`             | Shows if the customer churned (i.e., stopped using the company's services)       |
""")
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.info('Log in to access the page')
    st.code("""
            usernames:felixkwemoi
            password: FKM#101""")