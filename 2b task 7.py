def print_fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    a, b = 0, 1
    print(f"Fibonacci series up to {n} terms:")
    
    for _ in range(n):
        print(a, end=" ")
        # Update values: next term is the sum of the previous two
        a, b = b, a + b

# Example usage:
if __name__ == "__main__":
    n_terms = int(input("Enter the number of terms: "))
    print_fibonacci(n_terms)