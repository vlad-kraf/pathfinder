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


    def find_neighbours(self):
        x=0
        for row in self.grid:
            y=0
            for elem in row:
                # fill in point coordinates.
                self.neighbours[x,y] = []

                # fill in coordinates of point's neighbours.        
                if 0 <= y-1 <= self.height:
                    self.neighbours[x,y].append((x, y-1))

                if 0 <= y+1 <= self.height:
                    self.neighbours[x,y].append((x, y+1))

                if 0 <= x-1 <= self.width:
                    self.neighbours[x,y].append((x-1, y))

                if 0 <= x+1 <= self.width:
                    self.neighbours[x,y].append((x+1, y))
                y+=1
            x+=1 


    def put_wall(self, x, y):
        self.walls.append((x,y))

    def breadth_search(self, start):
        # breadth search algorithm for searching ways from start pointt to all other points on map.
        self.find_neighbours()

        frontier = collections.deque()
        frontier.append(start)
        self.came_from = {}
        self.came_from[start] = None

        while not len(frontier) == 0:
            current = frontier.popleft()
            for next in self.neighbours[current]:
                if next not in self.came_from and next not in self.walls:
                    frontier.append(next)
                    self.came_from[next] = current
        return self.came_from


    def reconstruct_path(self, start, goal):
        # reconstracttion of the path from goal-poiny to the start-point
        current = goal
        self.path = []
        while current != start:
            self.path.append(current)
            current = self.came_from[current]
        self.path.append(start) # optional
        self.path.reverse() # optional
        return self.path

    def get_path_map(self):
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
finish = (4, 4)

graph = Grid()
graph.put_wall(0, 3)
graph.put_wall(1, 3)
graph.put_wall(1, 2)
graph.breadth_search(start)
graph.reconstruct_path(start,finish)
print(graph.get_path_map())