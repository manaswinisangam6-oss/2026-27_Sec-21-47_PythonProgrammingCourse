# Create a set
s = {10, 20, 30, 40}
print("Original set:", s)

# Membership testing
print("20 in set:", 20 in s)
print("50 in set:", 50 in s)

# Add an element
s.add(50)
print("After add:", s)

# Remove an element
s.remove(20)
print("After remove:", s)

# Discard an element
s.discard(30)
print("After discard:", s)