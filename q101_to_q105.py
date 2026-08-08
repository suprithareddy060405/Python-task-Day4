# Question 101: Use underscores as digit separators in a large int.
# Hint / what to practice: 1_000_000.
def show_digit_separators():
    """
    Demonstrates using underscores as visual separators in a large integer.
    """
    large_int = 1_000_000
    print(f"Variable defined as 1_000_000. Value printed: {large_int}")
    print(f"Is 1_000_000 equal to 1000000? {large_int == 1000000}")


# Question 102: Predict 7/2, 7//2, 7%2, 7**2.
# Hint / what to practice: 3.5, 3, 1, 49.
def predict_operators():
    """
    Prints the predictions and actual outputs for arithmetic operations on 7 and 2.
    """
    ops = {
        "7 / 2 (True division)": 7 / 2,
        "7 // 2 (Floor division)": 7 // 2,
        "7 % 2 (Modulo / Remainder)": 7 % 2,
        "7 ** 2 (Exponentiation)": 7 ** 2
    }
    for desc, val in ops.items():
        print(f"{desc} = {val}")


# Question 103: Explain why 0.1 + 0.2 != 0.3.
# Hint / what to practice: Binary float representation.
def explain_floating_point_imprecision():
    """
    Returns an explanation of why 0.1 + 0.2 does not exactly equal 0.3 in Python (and computer arithmetic).
    """
    actual_sum = 0.1 + 0.2
    explanation = (
        f"Explanation:\n"
        f"0.1 + 0.2 actually equals: {actual_sum}\n"
        f"This is because computers represent numbers using binary floating-point (base 2).\n"
        f"Many decimal fractions (like 0.1 and 0.2) cannot be represented exactly in binary because\n"
        f"they become repeating decimals (similar to how 1/3 is 0.3333... in base 10).\n"
        f"Therefore, Python stores them as close approximations, and adding these approximations\n"
        f"results in a tiny rounding error that makes the sum slightly different from exactly 0.3."
    )
    return explanation


# Question 104: Check if a number is even using %.
# Hint / what to practice: n % 2 == 0.
def is_even(n: int) -> bool:
    """
    Returns True if n is even, False otherwise.
    """
    return n % 2 == 0

def demo_even_check():
    """
    Tests and prints results for even number checking.
    """
    test_numbers = [4, 7, 0, -2]
    for num in test_numbers:
        print(f"Is {num} even? {is_even(num)}")


# Question 105: Get the real and imaginary parts of 2+3j.
# Hint / what to practice: z.real, z.imag.
def get_complex_parts():
    """
    Gets and prints the real and imaginary parts of the complex number 2+3j.
    """
    z = 2 + 3j
    print(f"Complex number: z = {z}")
    print(f"Real part (z.real): {z.real}")
    print(f"Imaginary part (z.imag): {z.imag}")


if __name__ == "__main__":
    print("--- Question 101 ---")
    show_digit_separators()
    print("\n--- Question 102 ---")
    predict_operators()
    print("\n--- Question 103 ---")
    print(explain_floating_point_imprecision())
    print("\n--- Question 104 ---")
    demo_even_check()
    print("\n--- Question 105 ---")
    get_complex_parts()
