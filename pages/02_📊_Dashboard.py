import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import colorbrewer

st.set_page_config(
    page_title = "Dashboard page",
    page_icon = "📶",
    layout = 'wide'
)
st.title('CUSTOMER CHURN DASHBOARD')
st.sidebar.success("select a page above")

df = pd.read_excel("./data/data sets.xlsx")# loading the data to use in creating dashboard
#st.write(df)
def eda_dashboard():
    st.markdown("<h2 style='text-align: center; font-weight: bold;'>Exploratory Data Analysis</h2>", unsafe_allow_html=True)
    color=['#483d8b','#1d2951']
    col1,col2=st.columns(2)
    with col1:
        fig = px.bar(df, x='gender', color='Churn', 
                 color_discrete_sequence=color, 
                 title='Churning Split by Gender', 
                 labels={'count': 'Number of Customers'})
        st.plotly_chart(fig)
        
        fig = px.scatter(df, x='tenure', y='MonthlyCharges',color='Churn', 
             title='Tenure to MonthlyCharges Distribution', color_discrete_sequence=color)
        st.plotly_chart(fig)
    with col2:    
        fig = px.box(df,x='SeniorCitizen',y='TotalCharges',color='Churn',color_discrete_sequence=color,
                     title='Churning by TotalCharges and Senior Citizen')
        st.plotly_chart(fig)
        
        fig=px.bar(df,y='MonthlyCharges',x='Contract',color='Churn',
                title='Churn by MonthlyCharges and Contract',color_discrete_sequence=color)    
        st.plotly_chart(fig)
        
    fig = px.bar(df,x='PaymentMethod',y='TotalCharges',color='Churn',color_discrete_sequence=color,
                     title='Churn Distribution by PaymentMethod and TotalCharges')
    st.plotly_chart(fig)
        
    
        
        
    
    
    
def kpi_dashboard():
    st.markdown("<h2 style='text-align: center; font-weight: bold;'>Key Performance Indicators</h2>", unsafe_allow_html=True)  
    st.divider()  
      # Calculate KPIs
    churn_rate = (df['Churn'] == 'Yes').mean() * 100
    retention_rate = (df['Churn'] == 'No').mean() * 100

    # Create a DataFrame for the doughnut pie chart
    kpis_df = pd.DataFrame({
        'KPI': ['Churn Rate', 'Retention Rate'],
        'Rate': [churn_rate, retention_rate]
    })
    col1,col2=st.columns(2)
    
    st.markdown(f"""
                    <div style= "background-color:#1d2951;border-radius:10px;width:80%;margin-top:30px;">
                    <h3 style="marging-left:30px">Quick Stats about the data</h3>
                    <hr>
                    <h5 style="margin_left:30px">Data Size : {df.size}</h5>
                    <h5 style="margin_left:30px">Average Total Charges: ${df['TotalCharges'].mean():.2f}</h5>
                    <h5 style="margin_left:30px">Average MonthlyCharges: ${df['MonthlyCharges'].mean():.2f}</h5>           
                    <h5 style="margin_left:30px">Average Tenure:{df['tenure'].mean():.2f}</h5> 
                    <h5 style="margin_left:30px">Most Used Internet Service: {df[df['Churn'] == 'No']['InternetService'].mode().iloc[0]}</h5> 
                    """,unsafe_allow_html=True)
    with col1:
         ###  gauge for churn rate
        fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=churn_rate,
        #delta={'reference': 10},  # Change this to your target churn rate
        gauge={
            'axis': {'range': [0, 100]},
            'steps': [
                {'range': [0, 50], 'color': "#483d8b"},
                {'range': [50, 100], 'color': "#1d2951"}
            ],   
        },
        title={'text': "Churn Rate"}
    ))
        fig.update_layout(
        autosize=False,
        width=400,  # Adjust the width as needed
        height=300,  # Adjust the height as needed
        margin=dict(l=20, r=20, t=50, b=20)  # Adjust the margins as needed
    )
        st.plotly_chart(fig)
    with col2:    
         ### gauge for retention rate
        fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=retention_rate,
        #delta={'reference': 10},  # Change this to your target churn rate
        gauge={
            'axis': {'range': [0, 100]},
            'steps': [
                {'range': [0, 50], 'color': "#483d8b"},
                {'range': [50, 100], 'color': "#1d2951"}
            ],
        },
        title={'text': "Retention Rate"}
    ))
        fig.update_layout(
        autosize=False,
        width=400,  # Adjust the width as needed
        height=300,  # Adjust the height as needed
        margin=dict(l=20, r=20, t=50, b=20)  # Adjust the margins as needed
    )
        st.plotly_chart(fig)
 
 
 
 
if __name__ == '__main__':
    col1,col2=st.columns(2)
    with col1:
        pass
    with col2:
        st.selectbox("select dashboard to view",options=['KPI','EDA'],key='dashboard')
    if st.session_state['dashboard']=='KPI':
        kpi_dashboard()
        
    else:
        eda_dashboard()        


