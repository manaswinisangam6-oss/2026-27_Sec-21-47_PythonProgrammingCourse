1. Using for loop
print("For loop:", end=" ")
for i in range(1, 6):
    print(i, end=" ")
    if i == 3:
        break

# 2. Using while loop
print("\nWhile loop:", end=" ")
i = 1
while i <= 5:
    print(i, end=" ")
    if i == 3:
        break
    i += 1