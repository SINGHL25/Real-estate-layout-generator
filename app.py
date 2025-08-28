import streamlit as st
from engine.generator import generate_layout
from engine.visualizer_2d import plot_2d_layout
from engine.visualizer_3d import plot_3d_layout
from engine.cost_estimator import estimate_cost
from components.ui_inputs import user_input_form

st.set_page_config(page_title="AI Layout Generator", layout="wide")

st.title("🏢 AI-Powered Real Estate Layout Generator")

# Step 1: Get user inputs
user_inputs = user_input_form()

if st.button("Generate Layout"):
    layout = generate_layout(user_inputs)
    
    st.subheader("📐 2D Floor Plan")
    st.pyplot(plot_2d_layout(layout))

    st.subheader("🏗️ 3D Visualization")
    plot_3d_layout(layout)

    st.subheader("💰 Estimated Cost")
    st.write(estimate_cost(layout))

