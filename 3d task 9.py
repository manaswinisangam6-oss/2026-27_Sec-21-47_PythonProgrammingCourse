x = 50  # Global variable


def modify_variable():
  x = 100  # Local variable with the same name
  print(f"Inside function (local x): {x}")


print(f"Before function call (global x): {x}")
modify_variable()
print(f"After function call (global x): {x}")