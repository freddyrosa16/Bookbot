from stats import get_book_text, word_count, char_count


def main():
    print(f"Found {word_count('books/frankenstein.txt')} total words")
    print(char_count("books/frankenstein.txt"))


main()
