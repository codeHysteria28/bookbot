def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def count_words(text):
    text_split = text.split()
    word_count = len(text_split)

    return word_count

def main():
    file = get_book_text("./books/frankenstein.txt")
    words = count_words(file)

    print(f"Found {words} total words")

main()