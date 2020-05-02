grid = [[0 for _ in range(5)] for _ in range(5)]
neighbours = {}
height = 5-1
width = 5-1

walls = [(0, 3),(1, 3),(1, 2)]

def is_inside_field(vertex):
    x, y = vertex
    return 0 <= x <= width and 0 <= y <= height

def is_passable(vertex):
    return vertex not in walls 



x=0
for row in grid:
    y=0
    for elem in row:
        if (x, y) not in walls:
            neighbours[x,y] = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
            neighbours[x,y] = list(filter(is_inside_field, neighbours[x,y]))
            neighbours[x,y] = list(filter(is_passable, neighbours[x,y]))
        y+=1
    x+=1 


print(neighbours)