counter = 0  # Global variable


def increment_counter():
  global counter  # Tells Python to use the global variable
  counter += 1
  print(f"Inside function: {counter}")


print(f"Before calling function: {counter}")
increment_counter()
increment_counter()
print(f"After calling function: {counter}")