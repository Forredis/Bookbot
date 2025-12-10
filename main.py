from stats import *
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    source = sys.argv[1]

    with open(source) as f:
        text = f.read()

    words = num_of_words(text)
    characters = char_count(text)
    sorted_char = char_sort(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {source}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    
    for i in sorted_char:
        print(f"{i['char']}: {i['num']}")

main()