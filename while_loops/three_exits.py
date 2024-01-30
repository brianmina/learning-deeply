
prompt = "\nEnter 'quit' when you finished"
prompt += "What is your age?: "


movie_theater = True
while movie_theater:
    age = input(prompt)

    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age < 14:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")

    if age == 'quit':
        break
