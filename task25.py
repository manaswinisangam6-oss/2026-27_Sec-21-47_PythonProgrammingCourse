
# Campus Event Financial Planning

participants = int(input("Enter expected number of participants: "))

venue = float(input("Enter venue cost (Rs.): "))
equipment = float(input("Enter equipment cost (Rs.): "))
catering = float(input("Enter catering cost per participant (Rs.): "))
transport = float(input("Enter transport cost per participant (Rs.): "))
certificate = float(input("Enter certificate cost per participant (Rs.): "))

sponsorship = float(input("Enter available sponsorship (Rs.): "))
registration_fee = float(input("Enter registration fee per participant (Rs.): "))

if (participants <= 0 or min(
    venue, equipment, catering, transport,
    certificate, sponsorship, registration_fee
) < 0):
    print("Invalid input! Enter valid non-negative values.")
else:
    # Calculate costs
    fixed_cost = venue + equipment
    variable_cost = catering + transport + certificate
    total_variable_cost = variable_cost * participants
    total_cost = fixed_cost + total_variable_cost

    # Calculate income
    registration_income = participants * registration_fee
    total_funds = sponsorship + registration_income

    # Participant contribution after sponsorship
    remaining_cost = max(0, total_cost - sponsorship)
    contribution_per_participant = remaining_cost / participants

    # Sponsorship shortfall after registration income
    shortfall = max(0, total_cost - total_funds)
    surplus = max(0, total_funds - total_cost)

    # Break-even registration count
    contribution_margin = registration_fee - variable_cost
    required_funds = fixed_cost - sponsorship

    print("\n===== CAMPUS EVENT FINANCIAL REPORT =====")
    print(f"Venue cost: Rs. {venue:.2f}")
    print(f"Equipment cost: Rs. {equipment:.2f}")
    print(f"Catering cost: Rs. {total_variable_cost * 0 + catering * participants:.2f}")
    print(f"Transport cost: Rs. {transport * participants:.2f}")
    print(f"Certificate cost: Rs. {certificate * participants:.2f}")
    print(f"Total event cost: Rs. {total_cost:.2f}")
    print(f"Available sponsorship: Rs. {sponsorship:.2f}")
    print(f"Registration income: Rs. {registration_income:.2f}")
    print(f"Total funds: Rs. {total_funds:.2f}")
    print(f"Required contribution per participant after sponsorship: Rs. {contribution_per_participant:.2f}")

    if shortfall > 0:
        print(f"Sponsorship/funding shortfall: Rs. {shortfall:.2f}")
    else:
        print(f"Funding surplus: Rs. {surplus:.2f}")

    if contribution_margin > 0:
        if required_funds <= 0:
            break_even = 0
        else:
            break_even = int(
                (required_funds + contribution_margin - 1e-9)
                // contribution_margin
            )
            if break_even * contribution_margin < required_funds:
                break_even += 1

        print("Minimum registrations to break even:", break_even)

        if break_even <= participants:
            print("Result: Break-even is achievable with expected participants.")
        else:
            print("Result: More registrations are needed to break even.")
    else:
        print("Break-even is not achievable through registrations at this fee.")
        print("Increase the registration fee or reduce variable costs.")
