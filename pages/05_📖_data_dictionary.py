import streamlit as st

st.set_page_config(
    page_title = "Customer Data Dictionary",
    page_icon = "📚",
    layout = 'wide'
)

# Title
st.title("Customer Data Dictionary")
st.sidebar.success("select a page above")


# Markdown table
st.write("Overview of the data columns and their descriptions.")
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