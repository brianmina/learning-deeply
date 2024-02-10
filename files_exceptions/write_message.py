from pathlib import Path

contents = "I love my husband.\n"
contents += "I love him so much.\n"
contents += "I love him forever.\n"


path = Path('programming.txt')
path.write_text(contents)