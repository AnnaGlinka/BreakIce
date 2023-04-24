def create_matrix(row:int, col:int) -> list:
    two_dim_list = [[0 for c in range(col)] for r in range(row)]
    for r in range(row):
        for c in range(col):
            two_dim_list[r][c] = r * c
   
    return two_dim_list
    
    

i, j = [int(x) for x in (input("give 2 natural numbers separated by comma (row, col): ").split(","))]
print(create_matrix(i, j))