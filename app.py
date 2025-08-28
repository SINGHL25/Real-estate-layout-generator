# app.py
# app.py
import streamlit as st
from engine.cost_estimator import estimate_cost
from engine.generator import generate_layout
from engine.optimizer import optimize_layout
from engine.visualizer_2d import visualize_2d
from engine.visualizer_3d import visualize_3d  # Optional for direct import
import plotly.graph_objects as go



st.title("🏗 Construction Designer")

area = st.number_input("Enter total plot area (sqft)", min_value=100, value=1000)
unit_type = st.selectbox("Unit type", ["residential", "commercial"])
floors = st.slider("Number of floors", 1, 5, 1)
finish = st.selectbox("Finish level", ["standard", "luxury"])

# Estimate cost
cost = estimate_cost(area, unit_type, finish)
st.write("💰 Estimated Cost:", cost["estimated_cost"])

# Generate layout
layout = generate_layout(area, floors, unit_type)
optimized_layout = optimize_layout(layout)

st.write("📐 Layout Details:", optimized_layout)

# 2D Visualization
st.subheader("2D Layout")
st.pyplot(visualizer_2d.visualize_2d(optimized_layout))

# 3D Visualization
st.subheader("3D Layout")
fig = go.Figure()
for i, room in enumerate(optimized_layout["rooms"]):
    fig.add_trace(go.Bar3d(
        x=[i], y=[0], z=[0],
        dx=[1], dy=[1], dz=[len(room["name"])*2],
        name=room["name"]
    ))
fig.update_layout(title="3D Layout")
st.plotly_chart(fig)

