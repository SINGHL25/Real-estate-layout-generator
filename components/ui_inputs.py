import streamlit as st

def user_input_form():
    st.sidebar.header("Input Plot Details")
    
    plot_area = st.sidebar.number_input("Total Plot Area (sqft)", min_value=500, value=2000)
    floors = st.sidebar.number_input("Total Floors", min_value=1, value=3)
    purpose = st.sidebar.selectbox("Purpose", ["residential", "commercial", "mixed"])
    
    return {
        "plot_area": plot_area,
        "floors": floors,
        "purpose": purpose
    }

