from pathlib import Path


prompt = "\nEnter your name: "
prompt += "\n(Enter 'quit' to finish the program)"

guest_names = []

while True:
    names = input(prompt)
    if names == 'quit':
        break

    print(f"Thanks {names}!, Adding you to the guest list.")
    guest_names.append(names)
    print(guest_names)

file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

# path = Path('file_exceptions' / 'guest_book_new.txt')
path = Path('guest_book_new.txt')
path.write_text(file_string)