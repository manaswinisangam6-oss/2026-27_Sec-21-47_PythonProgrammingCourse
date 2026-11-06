def calculate_marks(subject1, subject2, subject3):
    total = subject1 + subject2 + subject3
    average = total / 3
    return total, average

# Example usage:
marks1, marks2, marks3 = 85, 90, 78
total_marks, average_marks = calculate_marks(marks1, marks2, marks3)

print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")