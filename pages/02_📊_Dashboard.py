import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(
    page_title="Dashboard Page",
    page_icon="📶",
    layout='wide'
)

# Title and sidebar success message
st.title('Customer Churn Analysis Dashboard')
st.sidebar.success("Select a page above")

st.write("""Welcome to the Telecommunication Customer Churn Analysis Dashboard. 
This interactive platform is designed to provide comprehensive insights into customer churn within the telecommunication industry. 
Navigate through the dashboard using the select box to explore two main sections: 
Key Performance Indicators (KPI) and Exploratory Data Analysis (EDA). 
The KPI section highlights critical metrics to understand overall churn rates and trends, 
while the EDA section delves into detailed data exploration to uncover underlying patterns and 
factors influencing customer churn. 
Use this tool to make data-driven decisions and enhance your strategies for customer retention.""")

# Load data
df = pd.read_excel("./data/data sets.xlsx")

# Define color scheme
color = ['#483d8b', '#1d2951']

def eda_dashboard():
    st.markdown("<h2 style='text-align: center; font-weight: bold;'>Exploratory Data Analysis</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        pass
    with col2:
        st.selectbox("select the type of E.D.A dashboard to view",options=['univariate dashboard','BI-Variate dashboard'],key='eda')
    if st.session_state['eda']=='univariate dashboard':
        st.subheader('Univariate Dashboard')
        col1, col2 = st.columns(2)
        with col1:
            ##defining categorical columns
            cat_columns = [column for column in df.columns if ((df[column].dtype)=='O') & (len(df[column].unique())>2)] 
            cat_columnsdf=df[cat_columns]
            ## countplot for categorical columns
# Define colors for the bars
            colors = ['pink', 'skyblue', 'purple','indigo']


# Plot countplots for each categorical column with annotations and custom colors
            for column in cat_columnsdf.columns:
                counts = cat_columnsdf[column].value_counts().reset_index()
                counts.columns = [column, 'count']
                fig = px.bar(counts, 
                x=column, 
                y='count', 
                title=f'Count of {column}')
                fig.update_traces(marker_color=colors[:len(counts)])
                fig.update_layout(xaxis_title=column, yaxis_title='Count')
                st.plotly_chart(fig)
            
    
        with col2:
            ##getting numeric columns
            numeric= [column for column in df.columns if ((df[column].dtype)!='O') & (len(df[column].unique())>2)]  
            numeric_columndf=df[numeric] 
            for column in numeric_columndf.columns:
                    fig=px.box(numeric_columndf,y=numeric_columndf[column],title = f"A visual representation of values in the  {column} column")
                    st.plotly_chart(fig)
    if st.session_state['eda']=='BI-Variate dashboard':
        colors = ['pink', 'skyblue', 'purple','indigo']
        st.subheader('BI-variate Dashboard')
        col1, col2 = st.columns(2)
        with col1:
            fig = px.scatter(df, x='tenure', y='MonthlyCharges', color='Churn', 
                         title='Tenure to MonthlyCharges Distribution', color_discrete_sequence=colors)
            st.plotly_chart(fig)
            fig = px.box(df, x='SeniorCitizen', y='TotalCharges', color='Churn', color_discrete_sequence=colors,
                     title='Churning by TotalCharges and Senior Citizen')
            st.plotly_chart(fig)
            
        with col2: 
            fig = px.bar(df, y='MonthlyCharges', x='Contract', color='Churn',
                     title='Churn by MonthlyCharges and Contract', color_discrete_sequence=colors)    
            st.plotly_chart(fig)
        
            fig = px.bar(df, x='PaymentMethod', y='TotalCharges', color='Churn', color_discrete_sequence=colors,
                 title='Churn Distribution by PaymentMethod and TotalCharges')
            st.plotly_chart(fig)
            
        numeric= [column for column in df.columns if ((df[column].dtype)!='O') & (len(df[column].unique())>2)] 
        correlation_matrix = df[numeric].corr()

        # Create a heatmap using Plotly
        heatmap = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.index,
        colorscale='RdBu',
        zmin=-1, zmax=1,
        text=correlation_matrix.values,
        texttemplate='%{text:.2f}',
        hoverongaps=False))

        heatmap.update_layout(title='Correlation Heatmap', xaxis_nticks=36)

# Display the heatmap in Streamlit
        st.plotly_chart(heatmap)
   
        
def kpi_dashboard():
    st.markdown("<h2 style='text-align: center; font-weight: bold;'>Key Performance Indicators</h2>", unsafe_allow_html=True)  
    st.divider() 
    # Calculate KPIs
    churn_rate = (df['Churn'] == 'Yes').mean() * 100
    retention_rate = (df['Churn'] == 'No').mean() * 100
    col1, col2 = st.columns(2)  
    with col1:
        # Gauge for retention rate
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=retention_rate,
            gauge={
                'axis': {'range': [0, 100]},
                'steps': [
                    {'range': [0, 50], 'color': "pink"},
                    {'range': [50, 100], 'color': "skyblue"}
                ],
            },
            title={'text': "Retention Rate"}
        ))
        fig.update_layout(width=400, height=200, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig)
    with col2:
        # Gauge for churn rate
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=churn_rate,
            gauge={
                'axis': {'range': [0, 100]},
                'steps': [
                    {'range': [0, 50], 'color': "pink"},
                    {'range': [50, 100], 'color': "skyblue"}
                ],
            },
            title={'text': "Churn Rate"}
        ))
        fig.update_layout(width=400, height=200, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig)
    churn_rate = (df['Churn'] == 'Yes').mean() * 100
    retention_rate = (df['Churn'] == 'No').mean() * 100
    avg_monthly_charge = df['MonthlyCharges'].mean()
    avg_total_charge = df['TotalCharges'].mean()
    avg_tenure = df['tenure'].mean()
    total_customers = len(df)
    churned_customers = len(df['Churn']=='Yes')
    
     
    # Define CSS for card visuals with background color and drop shadow
    st.write("""
            <style>
                .kpi-card {
                    background-color: black; /* Fading sky blue */
                    padding: 20px;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Shadow effect */
                    margin-bottom: 20px;
                    width: 300px; /* Set a fixed width for consistency */
                    display: inline-block;
                    margin-right: 20px;
                }
                .kpi-title {
                    font-size: 24px;
                    font-weight: bold;
                    margin-bottom: 10px;
                }
                .kpi-value {
                    font-size: 20px;
                    font-weight: bold;
                }
            </style>
        """, unsafe_allow_html=True)
 
 
    # 5.2 Display KPIs as card visuals with background color and drop shadow
    col1, col2, col3 = st.columns(3)
 
    with col1:
            st.markdown(f"<div class='kpi-card'><div class='kpi-title'>Total Customers 👫</div><div class='kpi-value'>{total_customers}</div></div>", unsafe_allow_html=True)
 
    with col2:
            st.markdown(f"<div class='kpi-card'><div class='kpi-title'>Churned Customers 🏃‍♂️</div><div class='kpi-value'>{churned_customers}</div></div>", unsafe_allow_html=True)
 
    with col3:
            st.markdown(f"<div class='kpi-card'><div class='kpi-title'>Churn Rate 📈</div><div class='kpi-value'>{churn_rate:.2f}%</div></div>", unsafe_allow_html=True)
 
    col4, col5, col6 = st.columns(3)
 
    with col4:
            st.markdown(f"<div class='kpi-card'><div class='kpi-title'>Avg Monthly Charge 💲</div><div class='kpi-value'>${avg_monthly_charge:.2f}</div></div>", unsafe_allow_html=True)
 
    with col5:
            st.markdown(f"<div class='kpi-card'><div class='kpi-title'>Avg Total Charge 💲</div><div class='kpi-value'>${avg_total_charge:.2f}</div></div>", unsafe_allow_html=True)
 
    with col6:
            st.markdown(f"<div class='kpi-card'><div class='kpi-title'>Avg Tenure ⏳(months)</div><div class='kpi-value'>{avg_tenure:.2f}</div></div>", unsafe_allow_html=True)
        
       
 
if __name__ == '__main__':
    col1,col2=st.columns(2)
    with col1:
        pass
    with col2:
        dashboard_selection = st.selectbox("Select dashboard to view", options=['KPI', 'EDA'], key='dashboard')
    if dashboard_selection == 'KPI':
        kpi_dashboard()
    else:
        eda_dashboard()
