def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."


# Example usage:
print(check_even_odd(4))  # Output: 4 is even.
print(check_even_odd(7))  # Output: 7 is odd.
print(check_even_odd(13))  # Output: 13 is odd.
