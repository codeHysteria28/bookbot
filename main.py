from stats import count_words
from stats import count_characters
from stats import report
import sys

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file = get_book_text(sys.argv[1])
    words = count_words(file)
    c = count_characters(file)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")

    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    print(report(c))

main()