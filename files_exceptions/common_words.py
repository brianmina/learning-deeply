from pathlib import Path


def count_words(filename):
    """count the word "the" of a file."""
    try:
        contents = filename.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        num_words = contents.split().count("the ")
        print(num_words)




books = ['book_1.txt', 'book_2.txt']

for book in books:
    filename = Path(book)
    count_words(filename)


