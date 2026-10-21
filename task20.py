
# Multi-Plan Telecommunications Cost Optimization

budget = float(input("Enter your budget (Rs): "))
required_validity = int(input("Enter required validity (days): "))
daily_data = float(input("Enter daily data usage (GB): "))
monthly_calls = int(input("Enter monthly call usage (minutes): "))

required_data = daily_data * 30

# Plan details: name, price, data (GB), calls (minutes), validity
plans = [
    ("Plan A", 199, 30, 1000, 28),
    ("Plan B", 299, 60, 2000, 56),
    ("Plan C", 399, 90, 3000, 84),
    ("Plan D", 249, 45, 1500, 30)
]

eligible_plans = []

for name, price, data, calls, validity in plans:
    excess_data = max(0, required_data - data)
    excess_calls = max(0, monthly_calls - calls)

    # Example excess charges
    extra_data_charge = excess_data * 10
    extra_call_charge = excess_calls * 0.50

    total_cost = price + extra_data_charge + extra_call_charge

    print("\nPlan:", name)
    print("Base price: Rs.", price)
    print("Excess data charge: Rs.", extra_data_charge)
    print("Excess call charge: Rs.", extra_call_charge)
    print("Total cost: Rs.", total_cost)

    if (validity >= required_validity
            and data >= required_data
            and calls >= monthly_calls
            and total_cost <= budget):
        eligible_plans.append(
            (total_cost, name, validity, data, calls)
        )

if eligible_plans:
    best = min(eligible_plans)

    print("\n--- Best Eligible Plan ---")
    print("Plan name:", best[1])
    print("Total cost: Rs.", best[0])
    print("Validity:", best[2], "days")
    print("Data allowance:", best[3], "GB")
    print("Call allowance:", best[4], "minutes")
else:
    print("\nNo eligible plan satisfies all requirements.")
