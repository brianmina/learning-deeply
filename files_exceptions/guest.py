from pathlib import Path

user_info = input("\nEnter your name:\n\t - ")

path = Path("guest.txt")
path.write_text(user_info)
