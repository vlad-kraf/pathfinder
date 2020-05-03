import collections



class Grid():
    def __init__(self, width=5, height=5):
        """ Class describes squared graph with equally weighted edges. 
            Has methods of creating walls, start ang goal-points, searching of 
            the path between start and goal."""
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.height = height-1
        self.width = width-1
        self.came_from = {}
        self.walls = []
        self.neighbours = {}
        self.start = ()
        self.goal = ()
        self.path = []

    def set_start_goal(self, start, goal):
        self.start = start
        self.goal = goal

    def create_wall(self, x, y):
        self.walls.append((x,y))

    def is_within_grid(self, vertex):
        x, y = vertex
        return 0 <= x <= self.width and 0 <= y <= self.height

    def is_passable(self, vertex):
        return vertex not in self.walls 

    def find_neighbours(self):
        # Creating dict with every vertex coordinates as keys, and list of 
        # it's neighbours coordinates as values.
        # Exceptions: walls and neighbours with coordinates that outside the grid.
        x=0
        for row in self.grid:
            y=0
            for vertex in row:
                if (x, y) not in self.walls:
                    self.neighbours[x,y] = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
                    self.neighbours[x,y] = list(filter(self.is_within_grid, self.neighbours[x,y]))
                    self.neighbours[x,y] = list(filter(self.is_passable, self.neighbours[x,y]))
                y+=1
            x+=1 

    def breadth_first_search(self):
        # Breadth first search algorithm for searching ways from start point 
        # to every existing point on map, except walls.
        self.find_neighbours()

        frontier = collections.deque()
        frontier.append(self.start)
        self.came_from = {}
        self.came_from[self.start] = None

        while not len(frontier) == 0:
            current = frontier.popleft()

            # Stops search when goal-point is found.
            if current == self.goal:
                break

            for next in self.neighbours[current]:
                if next not in self.came_from:
                    frontier.append(next)
                    self.came_from[next] = current
        return self.came_from

    def reconstruct_path(self):
        # Reconstraction of the path between start and goal points. 
        # Path represented as a list of coordinates, in order from start-point to goal-point.
        current = self.goal
        self.path = []
        while current != self.start:
            self.path.append(current)
            current = self.came_from[current]
        self.path.append(self.start)
        self.path.reverse()
        return self.path

    
    def show_path_on_grid(self):
        for k, v in self.came_from.items():
            x, y = k
            self.grid[y][x]=0 # attended vertexes
        
        for each in graph.path:
            x, y = each
            self.grid[y][x]=1 # path vertexes
        
        for each in graph.walls:
            x, y = each
            self.grid[y][x]=2 # walls vertexes
            
        string = ""
        for row in self.grid:
            for tile in row:
                string += str(tile)+" "
            string += "\n"
        return string





graph = Grid(width=20, height=20)
graph.create_wall(0, 3)
graph.create_wall(1, 3)
graph.create_wall(2, 3)
graph.create_wall(3, 3)
graph.create_wall(9, 0)
graph.create_wall(9, 1)
graph.create_wall(9, 2)
graph.create_wall(9, 3)
graph.create_wall(9, 4)
graph.create_wall(9, 5)
graph.create_wall(9, 6)
graph.create_wall(9, 7)
graph.create_wall(9, 8)
graph.create_wall(9, 9)
graph.create_wall(9, 10)
graph.create_wall(8, 10)
graph.create_wall(7, 10)
graph.create_wall(6, 10)
graph.create_wall(5, 10)
graph.create_wall(4, 10)
graph.create_wall(3, 10)
graph.create_wall(2, 10)

graph.set_start_goal(start=(0, 0), goal=(19, 19))

graph.breadth_first_search()
graph.reconstruct_path()
print(graph.show_path_on_grid())
