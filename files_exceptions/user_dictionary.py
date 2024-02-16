from pathlib import Path
import json


def get_stored_user_info(path):
    """Get stored user information if available"""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None


def get_new_user_info(path):
    """Prompt for user information."""
    username = input("What is your username: ")
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
    contents = get_stored_user_info(path)
    if contents:
        verify_username = input(f"is your username '{contents['username']}'? (y/n): ")
        if verify_username == 'y':
            print(f"Welcome back {contents['username']}")
        else:
            get_new_user_info(path)
    else:
        contents = get_new_user_info(path)
        print(f"We'll remember you when you come back, {contents['username']}!")


greet_user()