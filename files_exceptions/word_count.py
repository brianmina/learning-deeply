from pathlib import Path


def count_words(filenames):
    """"Coutn the approximate number of words in a file"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = ['alice.txt', 'bob.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)
