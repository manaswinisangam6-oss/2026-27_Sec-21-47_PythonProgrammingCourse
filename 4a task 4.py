students = {
    "S101": {"name": "Aarav Sharma", "marks": 88},
    "S102": {"name": "Ananya Reddy", "marks": 94},
    "S103": {"name": "Rohan Verma", "marks": 79},
}

for student_id, info in students.items():
    print(f"Name: {info['name']}, Marks: {info['marks']}")