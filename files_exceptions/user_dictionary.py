from pathlib import Path
import json


def get_stored_user_infor(path):
    """Get stored user information if available"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Prompt for user information."""
    username = input("What is your name: ")
    first_name = input("Your first name: ")
    last_name = input("Your last name: ")

    user_dict = {
        "username": username,
        "first_name": first_name,
        "last_name": last_name
    }
    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict


def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        print(f"Welcome back {username}")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()