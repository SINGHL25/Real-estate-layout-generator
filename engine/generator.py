
def generate_layout(user_inputs):
    """
    Basic layout generation logic.
    Will later integrate optimization & AI design.
    """
    area = user_inputs["plot_area"]
    floors = user_inputs["floors"]
    purpose = user_inputs["purpose"]   # commercial / residential / mix
    
    layout = {
        "area": area,
        "floors": floors,
        "purpose": purpose,
        "rooms": []
    }
    
    # Example: simple division
    if purpose == "residential":
        layout["rooms"] = ["Living Room", "Kitchen", "Bedroom1", "Bedroom2"]
    elif purpose == "commercial":
        layout["rooms"] = ["Showroom", "Office", "Washroom"]
    else:
        layout["rooms"] = ["Showroom", "Office", "FlatA", "FlatB"]

    return layout
