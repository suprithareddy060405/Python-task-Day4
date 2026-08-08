# Question 106: Write a string with an apostrophe two different ways.
# Hint / what to practice: Double quotes or escape.
def print_apostrophe_strings():
    """
    Shows two different ways to write a string containing an apostrophe.
    """
    # Method 1: Using double quotes around the string
    method_1 = "Python's popularity is growing rapidly."
    
    # Method 2: Escaping the single quote with a backslash
    method_2 = 'Python\'s popularity is growing rapidly.'
    
    print(f"Method 1 (Double Quotes): {method_1}")
    print(f"Method 2 (Escape Character): {method_2}")


# Question 107: Write a 3-line string using triple quotes.
# Hint / what to practice: """...""".
def print_three_line_string():
    """
    Demonstrates writing a multiline string using triple quotes.
    """
    three_line_str = """Line 1: Python is fun.
Line 2: Python is powerful.
Line 3: Python is easy to learn."""
    print("Three-line string using triple quotes:")
    print(three_line_str)


# Question 108: Index the first and last character of a string.
# Hint / what to practice: s[0], s[-1].
def index_first_and_last_char():
    """
    Prints the first and last characters of a given string.
    """
    s = "Programming"
    first_char = s[0]
    last_char = s[-1]
    print(f"Original string: '{s}'")
    print(f"First character (s[0]): '{first_char}'")
    print(f"Last character (s[-1]): '{last_char}'")


# Question 109: Slice the first three characters of 'Python'.
# Hint / what to practice: s[0:3].
def slice_first_three_chars():
    """
    Slices and prints the first three characters of the string 'Python'.
    """
    s = "Python"
    sliced = s[0:3]  # or s[:3]
    print(f"Original string: '{s}'")
    print(f"Sliced first three characters (s[0:3]): '{sliced}'")


# Question 110: Get the length of a string.
# Hint / what to practice: len(s).
def print_string_length():
    """
    Demonstrates finding the length of a string using the len() function.
    """
    s = "I love Python programming!"
    length = len(s)
    print(f"String: '{s}'")
    print(f"Length of the string (len(s)): {length}")


if __name__ == "__main__":
    print("--- Question 106 ---")
    print_apostrophe_strings()
    print("\n--- Question 107 ---")
    print_three_line_string()
    print("\n--- Question 108 ---")
    index_first_and_last_char()
    print("\n--- Question 109 ---")
    slice_first_three_chars()
    print("\n--- Question 110 ---")
    print_string_length()
