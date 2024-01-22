def car_information(manufacture, model, **car_info):
    """Return a dictionary of a car information."""
    car_info["Manufacture"] = manufacture
    car_info["Model"] = model
    return car_info


car_1 = car_information("toyota", "2023", color="blue", tank="16")
print(car_1)

