
# Retail Billing with Multiple Discount Rules

n = int(input("Enter number of products: "))

products = []
subtotal = 0
total_tax = 0

# Category-specific tax rates
tax_rates = {
    "electronics": 18,
    "clothing": 5,
    "groceries": 0,
    "furniture": 12
}

# Process multiple products
for i in range(n):
    print(f"\nEnter details for product {i + 1}")

    name = input("Product name: ")
    category = input(
        "Category (electronics/clothing/groceries/furniture): "
    ).lower()
    price = float(input("Unit price (Rs.): "))
    quantity = int(input("Quantity: "))

    if category not in tax_rates:
        print("Invalid category! Tax rate set to 0%.")
        tax_rate = 0
    else:
        tax_rate = tax_rates[category]

    amount = price * quantity
    tax = amount * tax_rate / 100

    subtotal += amount
    total_tax += tax

    products.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "amount": amount,
        "tax_rate": tax_rate,
        "tax": tax
    })

# Threshold-based discount rules
if subtotal >= 5000:
    discount_rate = 10
elif subtotal >= 2000:
    discount_rate = 5
else:
    discount_rate = 0

discount = subtotal * discount_rate / 100

# Maximum concession limit
maximum_discount = 1000
discount = min(discount, maximum_discount)

# Final bill
grand_total = subtotal + total_tax - discount

# Generate itemized invoice
print("\n" + "=" * 65)
print("                 RETAIL STORE INVOICE")
print("=" * 65)

print(f"{'Product':<15}{'Qty':>5}{'Price':>10}"
      f"{'Amount':>12}{'Tax':>10}")

print("-" * 65)

for p in products:
    print(f"{p['name']:<15}{p['quantity']:>5}"
          f"{p['price']:>10.2f}{p['amount']:>12.2f}"
          f"{p['tax']:>10.2f}")

print("-" * 65)
print(f"Subtotal:                 Rs. {subtotal:.2f}")
print(f"Total tax:                Rs. {total_tax:.2f}")
print(f"Discount rate:            {discount_rate}%")
print(f"Discount amount:          Rs. {discount:.2f}")
print(f"Maximum concession:       Rs. {maximum_discount:.2f}")
print("-" * 65)
print(f"GRAND TOTAL:              Rs. {grand_total:.2f}")
print("=" * 65)
