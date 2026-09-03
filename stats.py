def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def word_count(file_path):
    text = get_book_text(file_path)
    words = text.split()
    return len(words)

def char_count(file_path):
    text = get_book_text(file_path).lower()
    characters = {}
    for character in text:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters

def sort_on(character_count):
    return character_count[1]

def chars_dict_to_sorted_list(file_path):
    count = char_count(file_path)
    new_count_lst = []
    for key in count:
        new_count_lst.append((key, count[key]))
    sorting_by_count = sorted(new_count_lst, reverse=True, key=sort_on)
    return sorting_by_count
