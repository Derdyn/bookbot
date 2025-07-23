def word_count():
    with open("./books/frankenstein.txt") as b:
        count = len(b.read().split())
    print(f"{count} words found in the document")


