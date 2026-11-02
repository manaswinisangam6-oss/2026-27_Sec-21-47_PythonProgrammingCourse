Python
n, s = int(input("Enter a number: ")), 0
while n > 0:
    s, n = s + n % 10, n // 10
print("Sum of digits:", s)