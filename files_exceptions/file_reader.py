from pathlib import Path


path = Path("pi_digits.txt")
contents = path.read_text()
# contents = contents.rstrip()


pi_string = ""
for line in contents.splitlines():
    pi_string += line


print(pi_string)
print(len(pi_string))