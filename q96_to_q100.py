# Question 96: State the LEGB lookup order.
# Hint / what to practice: Local, Enclosing, Global, Built-in.
def state_legb_order():
    """
    Returns an explanation of the LEGB variable lookup order in Python.
    """
    explanation = (
        "Explanation:\n"
        "LEGB stands for the order in which Python searches scopes for a variable name:\n"
        "1. L (Local): Names assigned in any way within a function (def or lambda), and not declared global.\n"
        "2. E (Enclosing-function locals): Name lookups in the local scope of any and all enclosing functions\n"
        "   (e.g., in nested functions, from inner to outer).\n"
        "3. G (Global / module): Names assigned at the top-level of a module file, or declared global in a def.\n"
        "4. B (Built-in): Names preassigned in the built-in names module (e.g., open, range, print, len)."
    )
    return explanation


# Question 97: Show a local variable is invisible outside its function.
# Hint / what to practice: NameError outside.
def local_variable_scope_demo():
    """
    Creates a local variable inside the function.
    """
    local_var = "I am local to local_variable_scope_demo"
    print(f"Inside function: local_var = {local_var}")

def try_access_local_var():
    """
    Demonstrates trying to access a local variable from outside its scope.
    """
    local_variable_scope_demo()
    try:
        # This will raise a NameError because local_var does not exist in this scope
        print(local_var)
    except NameError as e:
        print(f"Outside function: Raised exception: {type(e).__name__}: {e}")


# Question 98: Explain why parameters/returns beat globals.
# Hint / what to practice: Self-contained, easier to reason.
def explain_parameters_returns_vs_globals():
    """
    Returns an explanation of why passing parameters and returning values
    is superior to using global variables.
    """
    explanation = (
        "Explanation:\n"
        "Using parameters and return values is preferred over globals because:\n"
        "1. Modularity: Functions are self-contained and don't rely on or modify state outside themselves.\n"
        "2. Readability: It is clear what inputs a function requires and what output it produces.\n"
        "3. Reusability: The function can be reused with different arguments without side effects.\n"
        "4. Testability: Functions are easier to write unit tests for because they don't depend on global state.\n"
        "5. Concurrency: Avoids race conditions in multi-threaded programs."
    )
    return explanation


# Question 99: Create an int, a float, and a complex number; print each type.
# Hint / what to practice: type() on each.
def create_and_print_types():
    """
    Creates an int, a float, and a complex number, and prints their values and types.
    """
    my_int = 42
    my_float = 3.14
    my_complex = 2 + 3j
    
    print(f"Value: {my_int}, Type: {type(my_int)}")
    print(f"Value: {my_float}, Type: {type(my_float)}")
    print(f"Value: {my_complex}, Type: {type(my_complex)}")


# Question 100: Show that Python ints have no overflow (2**100).
# Hint / what to practice: Big number prints fine.
def show_no_integer_overflow():
    """
    Demonstrates that Python integers have arbitrary precision and do not overflow.
    """
    large_number = 2 ** 100
    print(f"2**100 = {large_number}")
    print(f"Type of 2**100: {type(large_number)}")


if __name__ == "__main__":
    print("--- Question 96 ---")
    print(state_legb_order())
    print("\n--- Question 97 ---")
    try_access_local_var()
    print("\n--- Question 98 ---")
    print(explain_parameters_returns_vs_globals())
    print("\n--- Question 99 ---")
    create_and_print_types()
    print("\n--- Question 100 ---")
    show_no_integer_overflow()
