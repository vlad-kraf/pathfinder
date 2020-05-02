import collections

class Grid():
    def __init__(self, width=5, height=5):
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.height = height-1
        self.width = width-1
        self.came_from = {}
        self.walls = []
        self.path = []
        self.neighbours = {}

    def create_wall(self, x, y):
        self.walls.append((x,y))

    def is_inside_field(self, vertex):
        x, y = vertex
        return 0 <= x <= self.width and 0 <= y <= self.height

    def is_passable(self, vertex):
        return vertex not in self.walls 

    def find_neighbours(self):
        x=0
        for row in self.grid:
            y=0
            for elem in row:
                if (x, y) not in self.walls:
                    self.neighbours[x,y] = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
                    self.neighbours[x,y] = list(filter(self.is_inside_field, self.neighbours[x,y]))
                    self.neighbours[x,y] = list(filter(self.is_passable, self.neighbours[x,y]))
                y+=1
            x+=1 


    def breadth_first_search(self, start):
        # breadth search algorithm for searching ways from start pointt to all other points on map.
        self.find_neighbours()

        frontier = collections.deque()
        frontier.append(start)
        self.came_from = {}
        self.came_from[start] = None

        while not len(frontier) == 0:
            current = frontier.popleft()
            for next in self.neighbours[current]:
                if next not in self.came_from:
                    frontier.append(next)
                    self.came_from[next] = current
        return self.came_from


    def reconstruct_path(self, start, goal):
        # reconstracttion of the path from goal-pointt to the start-point
        current = goal
        self.path = []
        while current != start:
            self.path.append(current)
            current = self.came_from[current]
        self.path.append(start) # optional
        self.path.reverse() # optional
        return self.path

    def show_path_ongrid(self):
        for each in graph.path:
            x, y = each
            self.grid[x][y]=1
        
        for each in graph.walls:
            x, y = each
            self.grid[x][y]="#"
            
        string = ""
        for row in self.grid:
            for tile in row:
                string += str(tile)+" "
            string += "\n"
        return string



start = (0, 0)
finish = (0, 4)

graph = Grid()
graph.create_wall(0, 3)
graph.create_wall(1, 3)
graph.create_wall(2, 3)
graph.create_wall(3, 3)

graph.breadth_first_search(start)
graph.reconstruct_path(start,finish)
print(graph.show_path_ongrid())