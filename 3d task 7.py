def shopping_cart(**products):
  total = 0
  for item, price in products.items():
    print(f"{item.capitalize()}: ₹{price}")
    total += price
  print(f"Total: ₹{total}")


# Calling the function
shopping_cart(apple=15, orange=12, mango=10)