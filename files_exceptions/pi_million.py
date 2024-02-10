from pathlib import Path


path = Path("pi_million_digits.txt")
contents = path.read_text()


pi_string = ""
for line in contents.splitlines():
    pi_string += line

print(f"{pi_string[:52]}...")
print(len(pi_string))


birthday = input("Enter your birthday, i the form mmddyy")
if birthday in pi_string:
    print("Your Birthday appears in the first millon of pi!")
else:
    print("sooooryyyyy!")