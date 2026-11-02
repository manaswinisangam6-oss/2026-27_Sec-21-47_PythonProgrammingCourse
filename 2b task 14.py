# 1. Using for loop
print("For loop:", end=" ")
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")

# 2. Using while loop
print("\nWhile loop:", end=" ")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=" ")