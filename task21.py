
# Railway Fare and Reservation Calculator

n = int(input("Enter number of passengers: "))
distance = float(input("Enter journey distance in km: "))

print("\nTravel Classes:")
print("1. Sleeper")
print("2. AC 3-Tier")
print("3. AC 2-Tier")

choice = int(input("Select travel class (1-3): "))

if choice == 1:
    travel_class = "Sleeper"
    rate = 1.5
    reservation_fee = 20
elif choice == 2:
    travel_class = "AC 3-Tier"
    rate = 3.0
    reservation_fee = 40
elif choice == 3:
    travel_class = "AC 2-Tier"
    rate = 4.0
    reservation_fee = 60
else:
    print("Invalid travel class!")
    exit()

# Distance slab multiplier
if distance <= 100:
    slab_rate = 1.0
elif distance <= 500:
    slab_rate = 1.1
else:
    slab_rate = 1.2

total_fare = 0
passenger_fares = []

for i in range(1, n + 1):
    age = int(input(f"Enter age of passenger {i}: "))

    base_fare = distance * rate * slab_rate

    if age < 5:
        concession = 1.0
    elif age < 12:
        concession = 0.5
    elif age >= 60:
        concession = 0.4
    else:
        concession = 0.0

    discounted_fare = base_fare * (1 - concession)

    if age < 5:
        reservation = 0
    else:
        reservation = reservation_fee

    fare = discounted_fare + reservation

    passenger_fares.append(fare)
    total_fare += fare

    print(f"\nPassenger {i}")
    print("Age:", age)
    print("Base fare: Rs.", round(base_fare, 2))
    print("Concession:", concession * 100, "%")
    print("Reservation fee: Rs.", reservation)
    print("Ticket fare: Rs.", round(fare, 2))

print("\nTotal reservation fare: Rs.", round(total_fare, 2))

cancel = input("Cancel all tickets? (yes/no): ").lower()

if cancel == "yes":
    penalty_rate = float(
        input("Enter cancellation penalty percentage: ")
    )

    if penalty_rate < 0 or penalty_rate > 100:
        print("Invalid cancellation penalty percentage.")
    else:
        penalty = total_fare * penalty_rate / 100
        refund = total_fare - penalty

        print("\n--- Cancellation Details ---")
        print("Original fare: Rs.", round(total_fare, 2))
        print("Cancellation penalty: Rs.", round(penalty, 2))
        print("Refund amount: Rs.", round(refund, 2))
else:
    print("Reservation confirmed!")
