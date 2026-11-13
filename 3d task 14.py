def find_gcd(a, b):
  """Calculates the Greatest Common Divisor (GCD) of two numbers

  using the Euclidean algorithm recursively.
  """
  # Base case: when b becomes 0, a is the GCD
  if b == 0:
    return abs(a)

  # Recursive step: apply the Euclidean algorithm
  return find_gcd(b, a % b)


# --- Example usage ---
num1, num2 = 48, 18
result = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")