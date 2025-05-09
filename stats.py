# def num_words(text):
#     words = text.split()
#     return len(words)

# def get_character_count(text):
#     char_count = {}
#     for c in text:
#         lowered = c.lower()
#         if lowered in char_count:
#             char_count[lowered] += 1
#         else:
#             char_count[lowered] = 1
#             return char_count
  
# def sort_char_count(dict):
#       return dict[num]

# def get_char_dict_sort_char_count(num_chars_dict):
#         sorted_dict = []
#         for ch in num_chars_dict:
#             sorted_dict.append({"char": ch, "num": num_chars_dict[ch]})
#             sorted_dict.sort(reverse=True, key=sort_char_count)
#             return sorted_dict
# stats.py
def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    """
    Counts how many times each character appears in the text.
    Converts all characters to lowercase to avoid duplicates.
    Returns a dictionary mapping each character (str) to its count (int).
    """
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts


def get_char_dict_sort_char_count(char_count):
    """
    Takes a dictionary of characters and their counts, and returns a sorted
    list of dictionaries. Each dictionary contains two key-value pairs:
      - 'char': The character itself.
      - 'num': The count of that character.
    
    Only alphabetical characters (letters) are included.
    The list is sorted from greatest to least by the count.
    """
    char_list = []
    for char, num in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": num})
    # Sort the list in descending order based on the count
    char_list.sort(key=lambda item: item["num"], reverse=True)
    return char_list
