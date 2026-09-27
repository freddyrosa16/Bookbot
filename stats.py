def chars_dict_to_sorted_list(char_count_dict, file_path):
    char_count_list = []
    count_dict = char_count(file_path)
    for key in count_dict:
        char_count_list.append((key, count_dict[key]))
    sorted_list_count = sorted(char_count_list, reverse=True, key=sort_on)
    return sorted_list_count


def sort_on(character_count):
    return character_count[1]


def char_count(file_path):
    char_count_dict = {}
    words = get_book_text(file_path)
    for char in words.lower():
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1
    return char_count_dict


def word_count(file_path):
    words = get_book_text(file_path).split()
    return len(words)


def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()
