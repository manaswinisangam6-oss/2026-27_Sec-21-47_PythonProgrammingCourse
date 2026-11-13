def fibonacci_term(n):
  """Returns the n-th Fibonacci number using recursion."""
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci_term(n - 1) + fibonacci_term(n - 2)


def generate_fibonacci_series(n_terms):
  """Generates a Fibonacci series up to n_terms using recursion."""
  if n_terms <= 0:
    return "Please enter a positive integer."

  # Generate each term using the recursive function
  series = [fibonacci_term(i) for i in range(n_terms)]
  return series


# --- Example usage ---
terms = 10
result = generate_fibonacci_series(terms)
print(f"Fibonacci series ({terms} terms): {result}")