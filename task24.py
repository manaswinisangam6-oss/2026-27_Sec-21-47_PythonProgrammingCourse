
# Multi-Currency Travel Budget Analysis

budget = float(input("Enter travel budget in INR: "))
fee_rate = float(input("Enter conversion fee percentage: "))
n = int(input("Enter number of expense categories: "))

expenses = []
total_spending = 0

for i in range(n):
    print(f"\nExpense Category {i + 1}")

    category = input("Enter category name: ")
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency code: ").upper()
    exchange_rate = float(
        input("Enter exchange rate (INR per currency unit): ")
    )

    if amount < 0 or exchange_rate <= 0:
        print("Invalid amount or exchange rate.")
        continue

    # Convert expense into INR
    converted_amount = amount * exchange_rate

    # Apply conversion fee
    if currency == "INR":
        conversion_fee = 0
    else:
        conversion_fee = converted_amount * fee_rate / 100

    final_amount = converted_amount + conversion_fee
    total_spending += final_amount

    expenses.append({
        "category": category,
        "currency": currency,
        "original": amount,
        "converted": converted_amount,
        "fee": conversion_fee,
        "total": final_amount
    })

# Display itemized report
print("\n========== TRAVEL EXPENSE REPORT ==========")

for expense in expenses:
    print(f"\nCategory: {expense['category']}")
    print(f"Original expense: {expense['original']:.2f} "
          f"{expense['currency']}")
    print(f"Converted amount: Rs. {expense['converted']:.2f}")
    print(f"Conversion fee: Rs. {expense['fee']:.2f}")
    print(f"Total expense: Rs. {expense['total']:.2f}")

print("\nTotal spending: Rs.", round(total_spending, 2))
print("Travel budget: Rs.", round(budget, 2))

# Budget comparison
difference = budget - total_spending

if difference > 0:
    print("Budget status: Within budget")
    print("Remaining budget: Rs.", round(difference, 2))
elif difference < 0:
    print("Budget status: Budget exceeded")
    print("Overspending: Rs.", round(abs(difference), 2))
else:
    print("Budget status: Exactly within budget")

# Identify largest expense category
if expenses:
    largest = max(expenses, key=lambda x: x["total"])
    print("\nLargest expense category:", largest["category"])
    print("Amount: Rs.", round(largest["total"], 2))
else:
    print("\nNo valid expenses entered.")
