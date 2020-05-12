import collections



class Map():
   
    """ Class describes squared map as a graph with equally weighted edges. Grid contains coordinates of every vretex in graph. 
        Has methods for creating map, setting walls, checking map cells on passability.

        0 - free space,
        1 - path,
        2 - wall,
        3 - start point,
        4 - end point.

    """
    
    def __init__(self, width: int = 40, height: int = 40):
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.height = height-1
        self.width = width-1
        self.start_point: set = (0, 0)
        self.end_point: set = (0, 0)
  

    def create_wall(self, x: int, y: int):
        self.grid[y][x] = 2

    def is_within_grid(self, vertex: tuple):
        x, y = vertex
        return 0 <= x <= self.width and 0 <= y <= self.height

    def is_passable(self, vertex: tuple):
        x, y = vertex
        return self.grid[y][x] != 2

    def set_start_point(self, x: int, y: int):
        for row in self.grid:
            if 3 in row:
                self.grid[mylist.index(row)][row.index(3)] = 0
        self.grid[y][x] = 3
        self.start_point = (x, y)

    def set_end_point(self, x: int, y: int):
        for row in self.grid:
            if 4 in row:
                self.grid[mylist.index(row)][row.index(4)] = 0
        self.grid[y][x] = 4
        self.end_point = (x, y)
    

class BreadthFirstSearch(Map):

    """ Class that describes breadth first algorithm for searching path from start-point to end_point"""

    def __init__(self, width=40, height=40):
        super().__init__(width=width, height=height)
        self.came_from = {}
        self.neighbours = {}
        self.path = []

    def _find_neighbours(self):
        # Creates dict with every vertex coordinates as keys, and list of 
        # it's neighbours coordinates as values.
        # Exceptions: walls and neighbours with coordinates that outside the grid.
        y=0
        for row in self.grid:
            x=0
            for vertex in row:
                if vertex != 2:
                    self.neighbours[x,y] = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
                    self.neighbours[x,y] = list(filter(self.is_within_grid, self.neighbours[x,y]))
                    self.neighbours[x,y] = list(filter(self.is_passable, self.neighbours[x,y]))
                x+=1
            y+=1

    def breadth_first_search(self):
        # Breadth first search algorithm for searching ways from start point 
        # to every existing point on map, except walls.
        self._find_neighbours()

        frontier = collections.deque()
        frontier.append(self.start_point)
        self.came_from = {}
        self.came_from[self.start_point] = None

        while not len(frontier) == 0:
            current = frontier.popleft()

            # Stops search when gend_point is found.
            if current == self.end_point:
                break

            for next in self.neighbours[current]:
                if next not in self.came_from:
                    frontier.append(next)
                    self.came_from[next] = current
        return self.came_from

    def reconstruct_path(self):
        # Reconstraction of the path between start and end_points. 
        # Path represented as a list of coordinates, in order from start-point to end_point.
        current = self.end_point
        self.path = []
        while current != self.start_point:
            self.path.append(current)
            current = self.came_from[current]
        self.path.append(self.start_point)
        self.path.reverse()
        return self.path

    
    def show_path_on_grid(self):
        for k, v in self.came_from.items():
            x, y = k
            self.grid[y][x]=0 # attended vertexes
        
        for each in self.path:
            x, y = each
            self.grid[y][x]=1 # path vertexes
            
        string = ""
        for row in self.grid:
            for tile in row:
                string += str(tile)+" "
            string += "\n"
        return string 


path = BreadthFirstSearch(width=40, height=40)
path.set_start_point(0, 0)
path.set_end_point(19, 19)

path.create_wall(0, 3)
path.create_wall(1, 3)
path.create_wall(2, 3)
path.create_wall(3, 3)
path.create_wall(9, 0)
path.create_wall(9, 1)
path.create_wall(9, 2)
path.create_wall(9, 3)
path.create_wall(9, 4)
path.create_wall(9, 5)
path.create_wall(9, 6)
path.create_wall(9, 7)
path.create_wall(9, 8)
path.create_wall(9, 9)
path.create_wall(9, 10)
path.create_wall(8, 10)
path.create_wall(7, 10)
path.create_wall(6, 10)
path.create_wall(5, 10)
path.create_wall(4, 10)
path.create_wall(3, 10)
path.create_wall(2, 10)




path.breadth_first_search()
path.reconstruct_path()
print(path.show_path_on_grid())