from city_function import city_country


def test_city_country():
    """do names like 'Bogota, Colombia' work?."""
    formatted_name = city_country('Bogota', 'Colombia')
    assert formatted_name == 'Bogota, Colombia!'