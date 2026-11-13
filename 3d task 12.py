def factorial(n):
  """Calculates the factorial of a non-negative integer using recursion."""
  # Handle edge cases and base case
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers.")
  if n == 0 or n == 1:
    return 1

  # Recursive step
  return n * factorial(n - 1)


# --- Example usage ---
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")