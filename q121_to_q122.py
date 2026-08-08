# Question 121: Explain why 'is None' is preferred over '== None'.
# Hint / what to practice: Identity of the singleton.
def explain_is_none_vs_equality():
    """
    Returns an explanation of why 'is None' is preferred over '== None' in Python.
    """
    explanation = (
        "Explanation:\n"
        "1. None is a singleton in Python, meaning there is only ever one instance of None in memory.\n"
        "2. The 'is' operator checks for object identity (checks if both operands point to the exact same\n"
        "   object in memory). The '==' operator checks for value equality (invoking the __eq__ method).\n"
        "3. Using 'is None' is faster and safer because it cannot be overridden. A user-defined class\n"
        "   could override the '__eq__' method to return True when compared with None (e.g. obj == None\n"
        "   returns True even if it's not None), which leads to bugs. 'is None' guarantees correct behavior."
    )
    return explanation


# Question 122: Compute the average of three test scores and print with 2 decimals.
# Hint / what to practice: sum/3, f-string.
def compute_and_print_average(score1: float, score2: float, score3: float):
    """
    Computes the average of three test scores and prints it formatted to 2 decimal places.
    """
    total = score1 + score2 + score3
    average = total / 3
    print(f"Scores: {score1}, {score2}, {score3}")
    print(f"Average: {average:.2f}")


if __name__ == "__main__":
    print("--- Question 121 ---")
    print(explain_is_none_vs_equality())
    print("\n--- Question 122 ---")
    compute_and_print_average(85.5, 90.0, 92.25)
