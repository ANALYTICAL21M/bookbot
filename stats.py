def words_count(text: str) -> int:
    """Counts the number of words in a given text.

    Args:
        text (str): The text to count words in.
    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)

def chars_count(text: str) -> int:
    """Counts the number of characters in a given text.

    Args:
        text (str): The text to count characters in.
    Returns:
        int: The number of characters in the text.
    """
    clean_text = text.lower()
    chars = {}
    for c in clean_text:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    return chars

def sort_dict(d: dict) -> list:
    """Converts a dictionary of characters and counts into a sorted list of dictionaries.
    
    Args:
        d (dict): Dictionary with characters as keys and counts as values.
    Returns:
        list: Sorted list of dictionaries (greatest to least by count).
    """
    def sort_on(dict_item):
        return dict_item["num"]
    
    # Convert dictionary to list of dictionaries
    char_list = []
    for char, count in d.items():
        char_list.append({"char": char, "num": count})
    
    # Sort from greatest to least
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
