from stats import count_words
from stats import count_characters

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    file = get_book_text("./books/frankenstein.txt")
    words = count_words(file)
    c = count_characters(file)

    print(f"Found {words} total words")
    print(c)

main()