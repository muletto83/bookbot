import sys
from stats import get_number_of_words, chars_counter, sort_chars_counts

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_number_of_words(text)
    chars_counts = chars_counter(text)
    sorted_char_counts = sort_chars_counts(chars_counts)

    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for item in sorted_char_counts:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read() to open a d

main()



#alternate way to solve this
'''def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
''' 
