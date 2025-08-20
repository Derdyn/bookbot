def get_book_text(path):
    with open(path) as f:
        get_contents = f.read()
    return get_contents

def word_count(book):
    text = get_book_text(book)
    count = len(text.split())
    return count

def main():
    count = word_count("./books/frankenstein.txt")
    print(f"{count} words found in the document")


main()
