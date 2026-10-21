
print("===== EMPLOYEE PAYROLL SYSTEM =====")

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

basic = float(input("Enter basic pay: Rs. "))
overtime_hours = float(input("Enter overtime hours: "))
incentive = float(input("Enter incentive: Rs. "))

if basic < 0 or overtime_hours < 0 or incentive < 0:
    print("Invalid input! Values cannot be negative.")

else:
    hra = basic * 0.20
    da = basic * 0.10
    overtime_pay = overtime_hours * 200

    gross = basic + hra + da + overtime_pay + incentive

    # Progressive deductions
    remaining = gross
    deduction = 0

    slab1 = min(remaining, 20000)
    deduction += slab1 * 0.05
    remaining -= slab1

    slab2 = min(remaining, 20000)
    deduction += slab2 * 0.10
    remaining -= slab2

    if remaining > 0:
        deduction += remaining * 0.15

    net_salary = gross - deduction

    print("\n========== SALARY STATEMENT ==========")
    print("Employee Name :", name)
    print("Employee ID   :", emp_id)
    print("--------------------------------------")
    print(f"Basic Pay     : Rs. {basic:.2f}")
    print(f"HRA (20%)     : Rs. {hra:.2f}")
    print(f"DA (10%)      : Rs. {da:.2f}")
    print(f"Overtime Pay  : Rs. {overtime_pay:.2f}")
    print(f"Incentive     : Rs. {incentive:.2f}")
    print("--------------------------------------")
    print(f"Gross Salary  : Rs. {gross:.2f}")
    print(f"Deduction     : Rs. {deduction:.2f}")
    print("--------------------------------------")
    print(f"Net Salary    : Rs. {net_salary:.2f}")
    print("======================================")
