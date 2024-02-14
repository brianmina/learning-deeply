from pathlib import Path


def read_names(filename):
    """Read the names of a file."""
    try:
        contents = filename.read_text()
    except FileNotFoundError:
        pass
    else:
        print(contents)


names = ['cats', 'tigers', "dogs"]
for name in names:
    file_path = Path(name)
    read_names(file_path)
