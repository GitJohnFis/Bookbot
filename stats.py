"""Module for computing text statistics.

This module provides functions for counting words, counting characters,
and converting and sorting character frequency data.
"""

def get_num_words(text):
    """
    Return the number of words in the given text.
    
    Args:
        text (str): The text to be evaluated.
        
    Returns:
        int: The total number of words in the text.
    """
    words = text.split()
    return len(words)


def count_characters(text):
    """
    Count the occurrences of each character in the text.
    
    Args:
        text (str): The text in which to count characters.
        
    Returns:
        dict: A dictionary where keys are characters and values are their respective counts.
    """
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts


def get_char_dict_sort_char_count(char_count):
    """
    Convert a character frequency dictionary into a sorted list of dictionaries.

    Each dictionary in the returned list contains keys 'char' for the character and 'num'
    for its frequency.
    The list is sorted in descending order by frequency.

    Args:
        char_counts (dict): A dictionary mapping characters to their counts.

    Returns:
        list: A list of dictionaries sorted by character count in descending order.
    """
    char_list = []
    for char, num in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": num})
    # Sort the list in descending order based on the count
    char_list.sort(key=lambda item: item["num"], reverse=True)
    return char_list
