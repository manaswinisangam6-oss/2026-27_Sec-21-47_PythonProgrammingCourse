n, rev = int(input("Enter a number: ")), 0
while n > 0:
    rev, n = rev * 10 + n % 10, n // 10
print("Reversed number:", rev)