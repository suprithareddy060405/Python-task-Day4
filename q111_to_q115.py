# Question 111: Concatenate and repeat strings.
# Hint / what to practice: + and *.
def concatenate_and_repeat():
    """
    Demonstrates string concatenation (+) and repetition (*).
    """
    str1 = "Hello"
    str2 = "World"
    
    # Concatenation
    concat_result = str1 + ", " + str2 + "!"
    # Repetition
    repeat_result = str1 * 3
    
    print(f"Concatenation ('{str1}' + ', ' + '{str2}' + '!'): {concat_result}")
    print(f"Repetition ('{str1}' * 3): {repeat_result}")


# Question 112: Uppercase, lowercase, and strip a string.
# Hint / what to practice: upper/lower/strip.
def string_manipulation_methods():
    """
    Demonstrates upper(), lower(), and strip() methods on a string.
    """
    s = "   Python Programming   "
    
    print(f"Original string: '{s}'")
    print(f"Uppercase (upper()): '{s.upper()}'")
    print(f"Lowercase (lower()): '{s.lower()}'")
    print(f"Stripped (strip()): '{s.strip()}'")


# Question 113: Split 'a,b,c' on commas.
# Hint / what to practice: split(',').
def split_comma_string():
    """
    Splits the string 'a,b,c' by commas and prints the resulting list.
    """
    s = "a,b,c"
    result = s.split(',')
    print(f"Original string: '{s}'")
    print(f"Split result (split(',')): {result}")


# Question 114: Explain why strings are immutable.
# Hint / what to practice: Methods return new strings.
def explain_string_immutability():
    """
    Returns an explanation of why strings are immutable in Python.
    """
    explanation = (
        "Explanation:\n"
        "In Python, strings are immutable, meaning once a string object is created, it cannot be modified.\n"
        "Methods that seem to modify a string (like upper(), replace(), or strip()) do not change\n"
        "the original string in place. Instead, they construct and return a completely new string object.\n"
        "This helps with performance (enables string interning/sharing), guarantees that string values\n"
        "remain constant when used as dictionary keys, and simplifies safety in concurrent code."
    )
    return explanation


# Question 115: Produce booleans from four comparisons.
# Hint / what to practice: >, ==, !=, <=.
def produce_booleans_from_comparisons():
    """
    Executes four comparisons using >, ==, !=, and <=, printing the boolean results.
    """
    x = 10
    y = 20
    
    comp1 = x > y
    comp2 = x == 10
    comp3 = x != y
    comp4 = x <= y
    
    print(f"Is {x} > {y}? {comp1}")
    print(f"Is {x} == 10? {comp2}")
    print(f"Is {x} != {y}? {comp3}")
    print(f"Is {x} <= {y}? {comp4}")


if __name__ == "__main__":
    print("--- Question 111 ---")
    concatenate_and_repeat()
    print("\n--- Question 112 ---")
    string_manipulation_methods()
    print("\n--- Question 113 ---")
    split_comma_string()
    print("\n--- Question 114 ---")
    print(explain_string_immutability())
    print("\n--- Question 115 ---")
    produce_booleans_from_comparisons()
