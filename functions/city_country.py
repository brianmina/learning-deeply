def city_country(name_city, name_country):
    """Return a string formatted"""
    city_and_country = f"{name_city}, {name_country}"
    return city_and_country.title()

city_name1 = city_country('cartagena', 'colombia')
city_name2 = city_country("mexico df", "mexico")
city_name3 = city_country("miami", "usa")

print(city_name1)
print(city_name2)
print(city_name3)
