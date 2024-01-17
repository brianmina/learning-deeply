def make_shirt(message="Hello", size="Large"):
    """ prints the size and the message printed on it."""
    print(f"This shirt is {size} size and has the message '{message.title()}' on it.")

make_shirt('I love python.')
make_shirt()
make_shirt(size="Medium", message="I love programming.")


def describe_city(city, country="Colombia"):
    """ indicates in which country this city is"""
    print(f"{city.title()} is a city of {country}")

describe_city("Bogota")
describe_city("Miami", "USA")
describe_city("Medellin")
