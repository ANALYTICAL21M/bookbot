import sys
from stats import words_count, chars_count, sort_dict

def get_book_text(filepath) -> str:
    """Reads the content of a book from a text file.

    Args:
        filepath (str): The path to the text file containing the book.
    Returns:
        str: The content of the book as a string.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    """Main function to demonstrate reading a book text file."""
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = words_count(text)
    chars = chars_count(text)
    sorted_chars = sort_dict(chars)
    
    # Print formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Print only alphabetic characters in sorted order
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")



if __name__ == '__main__':
    main()
