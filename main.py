"""BookBot main module.

This module reads a given book file, analyzes its content, and prints a formatted report.
"""

import sys
from stats import get_num_words, count_characters, get_char_dict_sort_char_count


def get_book_text(path):
    """
    Read and return the content of the book from the specified file path.

    Args:
        path (str): The file system path to the book.

    Returns:
        str: The contents of the book file.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    """
    Main entry point for BookBot.

    This function checks for a command-line argument specifying a book file path,
    reads and analyzes the file, then prints the word and character analysis report.
    """
    # Ensure a path to the book file is provided.
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # Use the second command line argument as the book path.
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    # Get and print word count.
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    # (Optionally, you can include the full report printing below.)
    char_counts = count_characters(text)
    sorted_chars = get_char_dict_sort_char_count(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
