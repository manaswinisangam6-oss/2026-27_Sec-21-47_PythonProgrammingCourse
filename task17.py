
def calculate_bill(units):
    energy = 0

    # Progressive consumption slabs
    energy += min(units, 100) * 2

    if units > 100:
        energy += min(units - 100, 100) * 3

    if units > 200:
        energy += min(units - 200, 300) * 5

    if units > 500:
        energy += (units - 500) * 7

    fixed_charge = 50
    surcharge = energy * 0.05

    # Rebate for consumption up to 100 units
    rebate = energy * 0.02 if units <= 100 else 0

    total = energy + fixed_charge + surcharge - rebate

    return energy, fixed_charge, surcharge, rebate, total


months = int(input("Enter number of months: "))
previous_bill = None

for i in range(1, months + 1):
    print("\nMonth", i)
    units = int(input("Enter units consumed: "))

    if units < 0:
        print("Invalid units. Enter a non-negative value.")
        continue

    energy, fixed, surcharge, rebate, total = calculate_bill(units)

    print("Energy Charge: Rs.", round(energy, 2))
    print("Fixed Charge: Rs.", round(fixed, 2))
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Total Bill: Rs.", round(total, 2))

    if previous_bill is not None:
        increase = total - previous_bill
        percentage = (increase / previous_bill * 100
                      if previous_bill > 0 else 0)

        if increase > 0:
            print("Bill Increase: Rs.", round(increase, 2))
            print("Increase Percentage:",
                  round(percentage, 2), "%")

            if percentage > 30:
                print("Alert: Unusual bill increase!")
        else:
            print("Bill did not increase.")

    previous_bill = total
