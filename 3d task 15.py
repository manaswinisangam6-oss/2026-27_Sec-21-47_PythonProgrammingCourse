from functools import reduce

# Sample list of item prices in INR
prices = [250, 1200, 450, 3000, 850]
print(f"Original prices: {prices}\n")

# 1. map(): Apply an 18% GST to each price using a lambda function
prices_with_gst = list(map(lambda x: round(x * 1.18, 2), prices))
print(f"1. map() - Prices with 18% GST: {prices_with_gst}")

# 2. filter(): Keep only the items that cost more than ₹1000 (after GST)
expensive_items = list(filter(lambda x: x > 1000, prices_with_gst))
print(f"2. filter() - Items costing more than ₹1000: {expensive_items}")

# 3. reduce(): Calculate the total cumulative bill amount using reduce()
total_bill = reduce(lambda acc, x: acc + x, prices_with_gst)
print(f"3. reduce() - Total bill amount: ₹{round(total_bill, 2)}")