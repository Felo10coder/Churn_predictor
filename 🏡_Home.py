import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title = "Home page",
    page_icon = "🏘️",
    layout = 'wide'
)

# Title and introduction
st.markdown('<h1 style="text-align: left;"><u><i><b>TELECOM CHURN PREDICTOR</b></i></u></h1>', unsafe_allow_html=True)
#st.title('***TELECOM CHURN PREDICTOR***')
st.sidebar.success("select a page above")
st.subheader("🔮 Predicting the Future! 🔮")


st.subheader("*Introduction:*")
st.write(""" 
*Welcome to "Telecom Churn Predictor", an innovative tool designed to help telecommunication companies proactively retain their customers.
In today's competitive market, understanding and anticipating customer churn is crucial for maintaining a loyal customer base.
Our project leverages advanced data analytics to predict customer churn, providing actionable insights to reduce turnover and enhance customer satisfaction.
By harnessing the power of predictive modeling, businesses can identify at-risk customers and implement targeted retention strategies, ultimately driving long-term growth and stability.*""")


# Image
image_url = "https://media.istockphoto.com/id/1481095189/photo/businesswoman-analyzes-profitability-of-working-company-with-digital-virtual-screen-graphics.webp?s=1024x1024&w=is&k=20&c=K_zLxKkGr0RN_VGR_KdS6OcM1ClvkfbL6bK5df7DiT4="
st.markdown(f'<img src="{image_url}" alt="Telecommunication Networks" width="800" height="300">', unsafe_allow_html=True)


st.write("""**Key Features:**
- **Accurate Prediction:** Utilize predictive modeling to anticipate customer churn with precision.
- **Data-Driven Decisions:** Leverage comprehensive customer data to inform strategic initiatives.
- **Proactive Retention:** Take preemptive measures to retain valuable customers and foster long-term loyalty.
- **Data Upload and Integration:** Seamlessly upload customer data from various sources in CSV format. Integrate with existing databases and CRM systems for real-time data analysis.
""")

# Footer
st.write("### Contact:")

st.write("*Gmail*: felixkwemoi7@gmail")

st.markdown("""
*LinkedIn*:  [LinkedIn](https://www.linkedin.com/in/felo10/)
""")

st.markdown("""
*Medium Article*:  [Medium Article](https://medium.com/@felixkwemoi7/predicting-customer-churn-in-telecommunications-a-machine-learning-approach-c0ada4c36925)
""")

st.markdown("""
*GitHub Repository*:  [GitHub Repository](https://github.com/Felo10coder/Churn_predictor)
""")






