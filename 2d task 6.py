# Demonstrate string formatting methods

name = "Ravi"
age = 20
marks = 85.5

# Using format()
print("Using format():")
print("My name is {} and I am {} years old.".format(name, age))

# Using f-strings
print("\nUsing f-strings:")
print(f"My name is {name} and I scored {marks} marks.")

# Using % operator
print("\nUsing % operator:")
print("My name is %s and I am %d years old." % (name, age))