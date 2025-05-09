# from stats import (
#     num_words,
#     get_character_count,
#     get_char_dict_sort_char_count,
# )
# def main():
#     if len(sys.argv) < 2:
#             print("Usage: python3 main.py <path_to_book>")
#             sys.exit(1)
#             path_to_book = sys.argv[1]
#             # path_to_book = "books/frankenstein.txt"
#             book_text = get_book_text(path_to_book)
#             num_words = get_num_words(book_text)
#             chars_sorted = get_character_count(book_text)
#             num_chars_dict = get_char_dict_sort_char_count(char_character_count)
#             print_report(path_to_book, num_words, num_chars_dict)
#             print(f"{num_words} found in the document")
            
        

# def print_report(path_to_book, num_words, num_chars_dict):
#     print("=========== BOOKBOT ===========")
#     print(f"Analyzing book found at {path_to_book}...")
#     print("----------- Word Count ----------")
#     print(f"Found {num_words} total words")
#     print("--------- Character Count -------")
#     for items in num_chars_dict:
#         if not item["char"].isalpha():
#             continue
#         print(f"{item['char']}: {item['num']}") 
#     print("========== END ===========")


#     main()
    

# def get_book_text(path_to_file):
#     """Reads the contents of a file and returns it as a string."""
#     with open(path_to_file, 'r') as f:
#         return f.read()
# import json

# def get_book_text(path_to_file):
#     """
#     Reads the entire content of the given file using efficient file handling.
#     Returns the text, or an empty string if an error occurs.
#     """
#     try:
#         with open(path_to_file, 'r', encoding='utf-8') as file:
#             return file.read()
#     except Exception as e:
#         print(f"Error reading file {path_to_file}: {e}")
#         return ""

# def analyze_book(book_text):
#     """
#     Analyzes the given book text.
#     Returns a dictionary containing:
#         - The total number of lines.
#         - The total number of words.
#         - The total number of characters.
#     """
#     lines = book_text.splitlines()  # Splitting efficiently line-by-line
#     num_lines = len(lines)
#     num_words = sum(len(line.split()) for line in lines)
#     num_chars = len(book_text)
    
#     return {
#         "lines": num_lines,
#         "words": num_words,
#         "characters": num_chars
#     }

# def save_analysis(analysis_data, output_file):
#     """
#     Saves the analysis results as a JSON file using proper file writing practices.
#     """
#     try:
#         with open(output_file, 'w', encoding='utf-8') as file:
#             json.dump(analysis_data, file, indent=4)
#         print(f"Analysis saved to {output_file}")
#     except Exception as e:
#         print(f"Error saving analysis to {output_file}: {e}")

# def main():
#     book_path = "books/frankenstein.txt"  # Update this path as needed
#     book_text = get_book_text(book_path)
    
#     if not book_text:
#         print("No book text to process. Exiting.")
#         return

#     # For demonstration, print a snippet (first 200 characters) of the book
#     print("Book content read successfully.\n")
#     print("Snippet of the book:\n" + book_text[:200] + "...\n")
    
#     # Analyze the book text to create a simple report
#     analysis = analyze_book(book_text)
    
#     print("Book Analysis:")
#     for key, value in analysis.items():
#         print(f"{key.title()}: {value}")

#     # Save the analysis to a JSON file for future reference
#     analysis_output_path = "books/frankenstein_analysis.json"
#     save_analysis(analysis, analysis_output_path)

# if __name__ == "__main__":
#     main()
import sys
from stats import get_num_words, count_characters, get_char_dict_sort_char_count

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
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
