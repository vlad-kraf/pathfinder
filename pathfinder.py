import collections



class Map():
   
    """ Class describes squared map as a grid (or graph with equally weighted edges). 
        Grid contains coordinates of every vretex in graph. 
        Has methods for creating map, setting walls, checking map cells on passability.

        0 - free space
        1 - path
        2 - wall
        3 - start point
        4 - end point

    """
    
    def __init__(self, width: int = 40, height: int = 40):
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.start_point: set = (0, 0)
        self.end_point: set = (0, 0)
        self.height = height
        self.width = width

    def unset_wall(self, x: int, y: int):
        self.grid[y][x] = 0 

    def set_wall(self, x: int, y: int):
        self.grid[y][x] = 2

    def unset_start_point(self):
        for row in self.grid:
            if 3 in row:
                self.grid[mylist.index(row)][row.index(3)] = 0

    def set_start_point(self, x: int, y: int):
        self.unset_start_point()
        self.grid[y][x] = 3
        self.start_point = (x, y)
    
    def unset_end_point(self):
        for row in self.grid:
            if 4 in row:
                self.grid[mylist.index(row)][row.index(4)] = 0        

    def set_end_point(self, x: int, y: int):
        self.unset_end_point()
        self.grid[y][x] = 4
        self.end_point = (x, y)
    

class BreadthFirstSearch():

    """ Class that describes breadth first algorithm for searching path from start-point to end_point"""

    def __init__(self, map_: object):
        self.map_ = map_
        self.came_from = {}
        self.neighbours = {}
        self.path = []

    def is_within_grid(self, vertex: tuple):
        x, y = vertex
        return 0 <= x <= self.map_.width - 1 and 0 <= y <= self.map_.height - 1

    def is_passable(self, vertex: tuple):
        x, y = vertex
        return self.map_.grid[y][x] != 2

    def _find_neighbours(self):
        # Creates dict with every vertex coordinates as keys, and list of 
        # it's neighbours coordinates as values.
        # Exceptions: walls and neighbours with coordinates that outside the grid.
        y=0
        for row in self.map_.grid:
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

        frontier = collections.deque()
        frontier.append(self.map_.start_point)
        self.came_from = {}
        self.came_from[self.map_.start_point] = None

        while not len(frontier) == 0:
            current = frontier.popleft()

            # Stops search when gend_point is found.
            if current == self.map_.end_point:
                break

            for next in self.neighbours[current]:
                if next not in self.came_from:
                    frontier.append(next)
                    self.came_from[next] = current
        return self.came_from

    def reconstruct_path(self):
        # Reconstraction of the path between start and end_points. 
        # Path represented as a list of coordinates, in order from start-point to end_point.
        current = self.map_.end_point
        self.path = []
        while current != self.map_.start_point:
            self.path.append(current)
            current = self.came_from[current]
        self.path.append(self.map_.start_point)
        self.path.reverse()
        return self.path

    
    def grid_to_string(self):
        for k, v in self.came_from.items():
            x, y = k
            self.map_.grid[y][x]=5 # attended vertexes
        
        for each in self.path:
            x, y = each
            self.map_.grid[y][x]=1 # path vertexes
        
        x, y = self.map_.start_point
        self.map_.grid[y][x]=3

        x, y = self.map_.end_point
        self.map_.grid[y][x]=4
            
        string = ""
        for row in self.map_.grid:
            for tile in row:
                string += str(tile)+" "
            string += "\n"
        return string 

    def get_path(self):
        self._find_neighbours()
        self.breadth_first_search()
        self.reconstruct_path()

        return self.grid_to_string()

map_ = Map(width=40, height=40) 
map_.set_start_point(0, 0)
map_.set_end_point(19, 19)

map_.set_wall(0, 3)
map_.set_wall(1, 3)
map_.set_wall(2, 3)
map_.set_wall(3, 3)
map_.set_wall(9, 0)
map_.set_wall(9, 1)
map_.set_wall(9, 2)
map_.set_wall(9, 3)
map_.set_wall(9, 4)
map_.set_wall(9, 5)
map_.set_wall(9, 6)
map_.set_wall(9, 7)
map_.set_wall(9, 8)
map_.set_wall(9, 9)
map_.set_wall(9, 10)
map_.set_wall(8, 10)
map_.set_wall(7, 10)
map_.set_wall(6, 10)
map_.set_wall(5, 10)
map_.set_wall(4, 10)
map_.set_wall(3, 10)
map_.set_wall(2, 10)


finder = BreadthFirstSearch(map_)
print(finder.get_path())

