def calculate_simple_interest(principal, time, rate=5):
    """Calculates simple interest given principal, time (in years), and rate (percentage)."""
    return (principal * time * rate) / 100

# 1. Calling using the default rate (5%)
si_default = calculate_simple_interest(principal=10000, time=2)
print(f"Simple Interest (Default Rate): ₹{si_default}")

# 2. Calling with an explicit rate (e.g., 7.5%)
si_explicit = calculate_simple_interest(principal=10000, time=2, rate=7.5)
print(f"Simple Interest (Explicit Rate): ₹{si_explicit}")