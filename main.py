from stats import get_num_words
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    #print(text)
    word_count = get_num_words(text)
    #print(f"{word_count} words found in document.")
    chars = get_character_count(text)
    report(book_path,word_count,chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    character_count = {}
    for i in text.lower():
        if i in character_count:
            character_count[i] = character_count[i] + 1
        else:
            character_count[i] = 1
    return character_count

def report(book_path,word_count,chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for i in chars:
        print(f"The '{i}' character was found {chars[i]} times")
    print("--- End report ---")

main()