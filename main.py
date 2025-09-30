from stats import (
word_count,
char_count,
sort_count,
 )

def get_book_text(path):
    with open(path) as f:
        get_contents = f.read()
    return get_contents

def main():
    book = "./books/frankenstein.txt"
    text = get_book_text(book)
    count = word_count(text)
    chars = char_count(text)
    sorted = sort_count(chars)
    print_report(book, count, sorted)

def print_report(text, count, sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text}...")
    print("------------ Word Count ------------")
    print(f"Found {count} total words")
    print("------------ Character Count ------------")
    for i in sorted:
        if not i["char"].isalpha():
            continue
        print(f"{i['char']}: {i['num']}")
    print("------------ END ------------")

main()
