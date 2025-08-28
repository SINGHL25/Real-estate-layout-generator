
# visualizer_3d.py
import plotly.graph_objects as go

def visualize_3d(layout_json):
    """
    Dummy 3D visualization using plotly
    """
    fig = go.Figure()
    for i, room in enumerate(layout_json["rooms"]):
        fig.add_trace(go.Bar3d(
            x=[i], y=[0], z=[0],
            dx=[1], dy=[1], dz=[len(room["name"])*2],
            name=room["name"]
        ))
    fig.update_layout(title=f"{layout_json['unit_type']} Layout - 3D View")
    fig.show()

if __name__ == "__main__":
    from generator import generate_layout
    layout = generate_layout(2000)
    visualize_3d(layout)
