def word_count():
    with open("./books/frankenstein.txt") as b:
        count = len(b.read().split())
    print(f"{count} words found in the document")

def char_count():
    count = {}
    with open("./books/frankenstein.txt") as b:
        book = b.read()
        for char in book:
            count[char] = count.get(char, 0) +1
    return count
