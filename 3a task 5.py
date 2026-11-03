A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Addition
print("Addition:", [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)])

# Subtraction
print("Subtraction:", [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)])

# Multiplication
print("Multiplication:", [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)])