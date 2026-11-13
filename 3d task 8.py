def display_student_marks(**kwargs):
    for key, value in kwargs.items():
        formatted_key = key.replace("_", " ").title()
        print(f"{formatted_key}: {value}")


# Calling the function with student details and marks
display_student_marks(
    student_name="Ananya Sharma",
    mathematics=92,
    physics=88,
    chemistry=95,
    english=90
)