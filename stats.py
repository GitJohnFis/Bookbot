def num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1
            return char_count
  
def sort_char_count(dict):
      return dict[num]

def get_char_dict_sort_char_count(num_chars_dict):
        sorted_dict = []
        for ch in num_chars_dict:
            sorted_dict.append({"char": ch, "num": num_chars_dict[ch]})
            sorted_dict.sort(reverse=True, key=sort_char_count)
            return sorted_dict
