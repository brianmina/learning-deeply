print(" Enter two numbers, and I'll add them.")
print("Enter 'q' to quit.")


first_number = input("First number: ")
second_number = input("Second number: ")
try:
    answer = int(first_number) + int(second_number)
except ZeroDivisionError:
    print("soooooryyyy!")
except ValueError:
    print("soooooryyyy!")
else:
    print(answer)

