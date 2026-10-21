
name = input("Enter patient name: ")
age = int(input("Enter age: "))

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))
paid = float(input("Enter amount paid: "))

if not 0 <= age <= 120:
    print("Invalid age")

elif min(consultation, diagnostic, treatment, paid) < 0:
    print("Charges and payment cannot be negative")

else:
    gross = consultation + diagnostic + treatment

    if paid > gross:
        print("Invalid payment amount")

    else:
        concession_rate = 0

        if age >= 60:
            concession_rate += 10

        if gross >= 10000:
            concession_rate += 5

        concession = gross * concession_rate / 100
        final_bill = gross - concession
        balance = final_bill - paid

        if final_bill < 5000:
            category = "Category A"
        elif final_bill <= 15000:
            category = "Category B"
        else:
            category = "Category C"

        if balance == 0:
            status = "Fully Paid"
        elif paid == 0:
            status = "Unpaid"
        else:
            status = "Partially Paid"

        print("\n--- Hospital Bill ---")
        print("Patient:", name)
        print("Gross Bill: Rs.", gross)
        print("Concession:", concession_rate, "%")
        print("Concession Amount: Rs.", concession)
        print("Final Bill: Rs.", final_bill)
        print("Amount Paid: Rs.", paid)
        print("Balance Due: Rs.", balance)
        print("Payment Status:", status)
        print("Patient Classification:", category)
