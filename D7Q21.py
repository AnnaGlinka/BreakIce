"""
UP 5
DOWN 3
LEFT 3
RIGHT 2
"""
from math import sqrt

def calculate_distance(moves:list) -> int:
    x, y = 0, 0
    for move in moves:
        if move[0] == 'UP':
            y += int(move[1])
        if move[0] == 'DOWN':
            y -= int(move[1])
        if move[0] == 'RIGHT':
            x += int(move[1])
        if move[0] == 'LEFT':
            x -= int(move[1])
    return round(sqrt(x*x + y*y))
            


moves = []
while True:
    move = input()
    if not move:
        break
    moves.append(tuple(move.split(" ")))

print(calculate_distance(moves))