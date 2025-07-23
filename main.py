from stats import word_count

def get_book_text(path):
    with open(path) as f:
        get_contents = f.read()
    return get_contents

def main():
    book = get_book_text("./books/frankenstein.txt")
    print(book)


main()
word_count()
