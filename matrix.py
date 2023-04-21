# Initialize the matrix with 1's
matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

# Ask the user to input the row and column numbers to update
row = int(input("Enter the row number (1-3): "))
col = int(input("Enter the column number (1-3): "))

# Update the matrix with X at the specified row and column
matrix[row][col] = "X"

for i in range(row):
    print(row*col)
