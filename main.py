from stats import word_count, char_count, chars_dict_to_sorted_list


def main():
    print(f'Found {word_count("books/frankenstein.txt")} total words')
    print(f'{chars_dict_to_sorted_list("books/frankenstein.txt")}')

main()
