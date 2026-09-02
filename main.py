def main():
    print(f'Found {word_count("books/frankenstein.txt")} total words')

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def word_count(file_path):
    text = get_book_text(file_path)
    words = text.split()
    return len(words)

main()
