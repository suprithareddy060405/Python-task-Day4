# Question 116: List all the falsy values in Python.
# Hint / what to practice: 0, "", empty, None.
def list_falsy_values():
    """
    Returns an explanation and a list of all built-in falsy values in Python.
    """
    explanation = (
        "Explanation:\n"
        "In Python, the following values are considered 'falsy' (evaluate to False in a boolean context):\n"
        "1. Constants: None and False\n"
        "2. Numeric zero values: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)\n"
        "3. Empty sequences and collections: '' (empty string), () (empty tuple), [] (empty list),\n"
        "   {} (empty dictionary), set() (empty set), range(0)"
    )
    return explanation


# Question 117: Predict bool(0), bool('hi'), bool([]), bool(None).
# Hint / what to practice: F, T, F, F.
def predict_boolean_evaluations():
    """
    Evaluates and prints predictions for bool() evaluations.
    """
    evals = {
        "bool(0)": bool(0),
        "bool('hi')": bool('hi'),
        "bool([])": bool([]),
        "bool(None)": bool(None)
    }
    for expr, res in evals.items():
        print(f"{expr} evaluates to: {res}")


# Question 118: Count Trues in a list using sum().
# Hint / what to practice: True==1.
def count_trues_in_list():
    """
    Demonstrates counting occurrences of True in a list using the sum() function.
    """
    mixed_list = [True, False, True, True, False, True]
    # In Python, True is a subclass of int and has a value of 1, while False has a value of 0.
    # Therefore, sum() treats True as 1 and False as 0.
    true_count = sum(mixed_list)
    
    print(f"List: {mixed_list}")
    print(f"Number of Trues counted using sum(): {true_count}")


# Question 119: Create a None variable and test it with is None.
# Hint / what to practice: x is None.
def check_none_variable():
    """
    Creates a variable assigned to None and tests it using the 'is' operator.
    """
    x = None
    if x is None:
        print("x is indeed None (checked using 'x is None')")
    else:
        print("x is not None")


# Question 120: Show a function with no return gives None.
# Hint / what to practice: pass -> None.
def function_without_return():
    """
    A function with no explicit return statement.
    """
    pass

def demo_no_return_value():
    """
    Calls a function that has no return statement and prints its return value.
    """
    result = function_without_return()
    print(f"Function with no return statement returned: {result}")
    print(f"Is return value None? {result is None}")


if __name__ == "__main__":
    print("--- Question 116 ---")
    print(list_falsy_values())
    print("\n--- Question 117 ---")
    predict_boolean_evaluations()
    print("\n--- Question 118 ---")
    count_trues_in_list()
    print("\n--- Question 119 ---")
    check_none_variable()
    print("\n--- Question 120 ---")
    demo_no_return_value()
