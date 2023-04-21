# Initialize a 3x3 matrix with 1's
matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

# Ask user to input row and column numbers where they want to update the matrix
row = int(input("Enter row number (0-2): "))
col = int(input("Enter column number (0-2): "))

# Update the matrix with X at the specified row and column numbers
matrix[row][col] = "X"

# Print the updated matrix
for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()
