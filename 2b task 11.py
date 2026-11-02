n, temp, s = int(input("Enter a 3-digit number: ")), n, 0
while temp > 0:
    s, temp = s + (temp % 10) ** 3, temp // 10
print("Armstrong" if s == n else "Not Armstrong")