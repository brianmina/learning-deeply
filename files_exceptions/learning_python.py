from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

print(contents)


for line in contents.splitlines():
    new_word = line.replace("python", "C")
    print(new_word)