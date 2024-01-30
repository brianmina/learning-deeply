
prompt = "\nPlease enter the toppings you want:"
prompt += "\n(Enter 'quit' to exit).  -"


while True:
    toppings = input(prompt)

    if toppings != 'quit':
        print(f"\tAdding the followings toppings: \n-{toppings}.\nAnything else?")

