
# Manufacturing Cost and Profitability Analysis

units = int(input("Enter number of units produced: "))
material_cost = float(input("Enter material cost per unit (Rs.): "))
labour_cost = float(input("Enter labour cost per unit (Rs.): "))
wastage_rate = float(input("Enter wastage percentage: "))
machine_cost = float(input("Enter total machine cost (Rs.): "))
selling_price = float(input("Enter selling price per unit (Rs.): "))
profit_target = float(input("Enter profit target (Rs.): "))

if (units <= 0 or material_cost < 0 or labour_cost < 0
        or machine_cost < 0 or selling_price < 0
        or not 0 <= wastage_rate <= 100 or profit_target < 0):
    print("Invalid input! Enter valid non-negative values.")
else:
    # Calculate manufacturing costs
    total_material = units * material_cost
    wastage_cost = total_material * wastage_rate / 100
    total_labour = units * labour_cost

    total_cost = (
        total_material + wastage_cost
        + total_labour + machine_cost
    )

    cost_per_unit = total_cost / units
    revenue = units * selling_price
    profit = revenue - total_cost
    profit_percentage = (profit / total_cost * 100
                         if total_cost > 0 else 0)

    # Display cost analysis
    print("\n===== MANUFACTURING COST REPORT =====")
    print("Units produced:", units)
    print(f"Material cost: Rs. {total_material:.2f}")
    print(f"Wastage cost: Rs. {wastage_cost:.2f}")
    print(f"Labour cost: Rs. {total_labour:.2f}")
    print(f"Machine cost: Rs. {machine_cost:.2f}")
    print(f"Total manufacturing cost: Rs. {total_cost:.2f}")
    print(f"Cost per unit: Rs. {cost_per_unit:.2f}")
    print(f"Total sales revenue: Rs. {revenue:.2f}")
    print(f"Total profit/loss: Rs. {profit:.2f}")
    print(f"Profit percentage: {profit_percentage:.2f}%")
    print(f"Required profit target: Rs. {profit_target:.2f}")

    if profit >= profit_target:
        print("Result: Profit target achieved.")
    else:
        shortfall = profit_target - profit
        print("Result: Profit target not achieved.")
        print(f"Additional profit required: Rs. {shortfall:.2f}")

    if profit > 0:
        print("Status: PROFIT")
    elif profit < 0:
        print("Status: LOSS")
    else:
        print("Status: BREAK-EVEN")
