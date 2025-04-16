from stats import (
    num_words,
    get_character_count,
    get_char_dict_sort_char_count,
)
def main():
    if len(sys.argv) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
            path_to_book = sys.argv[1]
            # path_to_book = "books/frankenstein.txt"
            book_text = get_book_text(path_to_book)
            num_words = get_num_words(book_text)
            chars_sorted = get_character_count(book_text)
            num_chars_dict = get_char_dict_sort_char_count(char_character_count)
            print_report(path_to_book, num_words, num_chars_dict)
            print(f"{num_words} found in the document")
            
            
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
        

def print_report(path_to_book, num_words, num_chars_dict):
    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for items in num_chars_dict:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}") 
    print("========== END ===========")


    main()
    