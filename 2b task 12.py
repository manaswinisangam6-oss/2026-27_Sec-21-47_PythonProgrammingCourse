n, rev = int(input("Enter a number: ")), 0
temp = n
while temp > 0:
    rev, temp = rev * 10 + temp % 10, temp // 10
print("Palindrome" if rev == n else "Not Palindrome")