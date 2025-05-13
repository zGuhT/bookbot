from stats import get_num_words
from stats import get_num_chars
from stats import sort_on
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    word_count = get_num_words(file_contents)
    char_count = get_num_chars(file_contents)
    sorted_chars = sorted(char_count, key=sort_on, reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["name"].isalpha():
            print(f"{item["name"]}: {item["num"]}")
    print("============= END ===============")
    
main()