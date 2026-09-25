marks = float(input("Enter the total marks out of 100: "))

if marks >= 90:
    print("Grade A(marks={marks})")
elif marks >= 80:
    print("Grade B(marks={marks})")
elif marks >= 70:
    print("Grade C(marks={marks})")
else:
    print("Grade D(marks={marks})")