
# cost_estimator.py
def estimate_cost(area_sqft, construction_type="residential", finish_level="standard"):
    """
    Simple cost estimator based on area and type.
    """
    base_rate = 1200 if finish_level == "standard" else 1800
    multiplier = 1.2 if construction_type == "commercial" else 1.0
    total_cost = area_sqft * base_rate * multiplier
    return {"area_sqft": area_sqft, "type": construction_type, "finish": finish_level, "estimated_cost": total_cost}

if __name__ == "__main__":
    print(estimate_cost(1000))
