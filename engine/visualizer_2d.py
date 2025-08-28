
# visualizer_2d.py
import matplotlib.pyplot as plt

def visualize_2d(layout_json):
    """
    Dummy 2D visualization
    """
    fig, ax = plt.subplots()
    y = 0
    for room in layout_json["rooms"]:
        ax.barh(y, len(room["name"])*5, height=0.8)
        ax.text(len(room["name"])*2, y, room["name"], va='center', ha='center', color='white')
        y += 1
    ax.set_yticks([])
    ax.set_title(f"{layout_json['unit_type']} Layout - 2D View")
    plt.show()

if __name__ == "__main__":
    from generator import generate_layout
    layout = generate_layout(2000)
    visualize_2d(layout)
