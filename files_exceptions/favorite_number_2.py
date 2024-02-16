from pathlib import Path
import json

prompt = input("What is your favorite number?: ")

path = Path("favorite_number.json")
contents = json.dumps(prompt)
path.write_text(contents)
