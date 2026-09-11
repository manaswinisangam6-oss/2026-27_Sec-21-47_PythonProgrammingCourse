P=float(input("enter principal:"))
R=float(input("enter rate of interest:"))
T=float(input("enter time in year:"))
A=P*(1+R/100)**T
CI=A-P
print("compound interest=",CI)
print("amount=",A)