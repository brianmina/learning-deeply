def city_country(city_name, country_name, population_number=''):
    """Return a single string of city and country and """
    if population_number:
        formatted_city_name = f"{city_name}, {country_name},{population_number}!"
    else:
        formatted_city_name = f"{city_name}, {country_name}!"

    return formatted_city_name.title()
