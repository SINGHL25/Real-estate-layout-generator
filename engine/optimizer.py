
# optimizer.py
def optimize_layout(layout_json):
    """
    Dummy optimizer: sorts rooms alphabetically
    """
    layout_json["rooms"].sort(key=lambda x: x["name"])
    layout_json["optimized"] = True
    return layout_json

if __name__ == "__main__":
    from generator import generate_layout
    layout = generate_layout(2000)
    print(optimize_layout(layout))
