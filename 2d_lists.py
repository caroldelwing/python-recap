number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7,8, 9]
]

print(number_grid[0][0])

#Print all lists inside number_grid
for row in number_grid:
    print(row)

#NESTED LOOP: Print all elements inside each row of number_grid
for row in number_grid:
    for column in row:
        print(column)