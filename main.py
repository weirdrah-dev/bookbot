def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count = get_book_length(text)
    print(f"{word_count} words found in document.")
    print(get_character_count(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_length(text):
    book_words = text.split()
    return len(book_words)

def get_character_count(text):
    character_count = {}
    for i in text.lower():
        if i in character_count:
            character_count[i] = character_count[i] + 1
        else:
            character_count[i] = 1
    return character_count

main()