def create_matrix(row: int, col: int) -> list:
    matrix = [[c * r for c in range(col)] for r in range(row) ]
    return matrix

row, col = map(int, input("Give number of rows and colums (serparated by a comman: ").split(","))
print(row, col)
print(create_matrix(row, col))
