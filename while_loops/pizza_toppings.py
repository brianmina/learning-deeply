
prompt = "\nPlease enter the toppings you want:"
prompt += "\n(Enter 'quit' to exit).    --"

toppings = ""

while toppings:
    user_input = input(prompt)
    if user_input != 'quit':
        print(f"\nAdding the followings toppings: \n{user_input}