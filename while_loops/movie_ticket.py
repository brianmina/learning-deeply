
prompt = "\n what is your age?: "

while True:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age < 14:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")

