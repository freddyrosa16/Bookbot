from stats import word_count, char_count, chars_dict_to_sorted_list


def main():
    print_report("books/frankenstein.txt", word_count, chars_dict_to_sorted_list)

def print_report(file_path, word_count, sorted_lst):
    count = word_count(file_path)
    sorted_lst = chars_dict_to_sorted_list(file_path)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...')
    print('----------- Word Count ----------')
    print(f'Found {count} total words')
    print('--------- Character Count -------')
    for key in sorted_lst:
        if key[0].isalpha():
            print(f'{key[0]}: {key[1]}')
    print('============= END ===============')

main()
