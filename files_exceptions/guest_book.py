from pathlib import Path


path = Path("guest_book.txt")

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

file_string = ""
for names in guest_names:
    file_string += f"{names}"

path.write_text(file_string)