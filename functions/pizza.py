def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"f -{topping}")

make_pizza(16,"pepperoni")
make_pizza(12,"mushrooms", "greens peppers")