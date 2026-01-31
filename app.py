def add_numbers(a: int, b: int) -> int:
    """Adds two integers and returns the result."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")
    return a + b


if __name__ == "__main__":
    RESULT = add_numbers(5, 10)
    print(f"The sum is: {RESULT}")
