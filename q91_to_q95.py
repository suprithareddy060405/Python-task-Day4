# Question 91: Define global vs local scope in your own words.
# Hint / what to practice: Outside vs inside a function.
def explain_global_vs_local_scope():
    """
    Returns an explanation of the difference between global and local scope.
    """
    explanation = (
        "Explanation:\n"
        "1. Global Scope: A variable declared outside of any function exists in the global scope.\n"
        "   It is accessible from anywhere in the file (inside or outside functions) after its definition.\n"
        "2. Local Scope: A variable declared inside a function exists only within that function's local scope.\n"
        "   It is created when the function is called and is destroyed when the function returns.\n"
        "   It cannot be accessed from outside that function."
    )
    return explanation


# Question 92: Show a function reading a global variable.
# Hint / what to practice: Just reference it.
global_var = "I am a global variable"

def read_global_variable():
    """
    Demonstrates reading a global variable inside a function.
    """
    print(f"Inside function (reading global_var): {global_var}")


# Question 93: Explain why increment without global fails.
# Hint / what to practice: Assignment makes it local.
def explain_increment_failure():
    """
    Returns an explanation of why attempting to increment a global variable
    without using the 'global' keyword fails.
    """
    explanation = (
        "Explanation:\n"
        "When you use an assignment statement (like x += 1 or x = x + 1) inside a function,\n"
        "Python automatically treats that variable as local to the function. If you try to\n"
        "read its value before assigning to it (which += 1 does, because it reads the current\n"
        "value to add to it), Python throws an UnboundLocalError because it assumes you are trying\n"
        "to access a local variable that hasn't been defined yet."
    )
    return explanation


# Question 94: Fix a counter function using the global keyword.
# Hint / what to practice: global count.
counter = 0

def increment_counter():
    """
    Uses the 'global' keyword to modify the global counter variable.
    """
    global counter
    counter += 1
    print(f"Counter incremented to: {counter}")


# Question 95: Explain 'local variable referenced before assignment'.
# Hint / what to practice: Local made for whole function.
def explain_referenced_before_assignment():
    """
    Returns an explanation of 'UnboundLocalError: local variable referenced before assignment'.
    """
    explanation = (
        "Explanation:\n"
        "This error occurs when Python parses a function and sees an assignment to a variable,\n"
        "marking it as a local variable for the *entire* scope of that function. If there is a line\n"
        "of code that tries to read or use that variable before the line where it is assigned,\n"
        "Python raises an UnboundLocalError: local variable referenced before assignment.\n"
        "Even if a global variable with the same name exists, Python ignores it because it decided\n"
        "the variable name is local due to the assignment later in the function."
    )
    return explanation


if __name__ == "__main__":
    print("--- Question 91 ---")
    print(explain_global_vs_local_scope())
    print("\n--- Question 92 ---")
    read_global_variable()
    print("\n--- Question 93 ---")
    print(explain_increment_failure())
    print("\n--- Question 94 ---")
    print(f"Initial counter: {counter}")
    increment_counter()
    increment_counter()
    print("\n--- Question 95 ---")
    print(explain_referenced_before_assignment())
