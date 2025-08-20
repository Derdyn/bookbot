from stats import word_count

def get_book_text(path):
    with open(path) as f:
        get_contents = f.read()
    return get_contents

def main():
    book = "./books/frankenstein.txt"
    text = get_book_text(book)
    count = word_count(text)
    print(f"{count} words found in the document")


main()
