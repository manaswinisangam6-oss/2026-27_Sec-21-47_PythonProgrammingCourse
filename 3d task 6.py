def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Calling the function
print_details(name="Krishna", age=26, city="Guntur")