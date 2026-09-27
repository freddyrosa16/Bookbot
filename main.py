import sys
from stats import get_book_text, word_count, char_count, chars_dict_to_sorted_list


def print_report(file_path, word_count, chars_dict_to_sorted_list):
    count = word_count(sys.argv[1])
    lst = chars_dict_to_sorted_list(char_count, sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in lst:
        if i[0].isalpha():
            print(f"{i[0]}: {i[1]}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print_report(sys.argv[1], word_count, chars_dict_to_sorted_list)


main()
