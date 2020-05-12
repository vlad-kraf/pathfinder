import sys

import pygame

import pathfinder



# Global constants
GREEN = (144, 190, 109) # available for use cells
BROWN = (154, 140, 152) # path cells
GRAY = (87, 117, 144) # wall cells
BLUE = (224, 251, 252) # background
 
WINDOW_SIZE = [800, 640] # game window size

# Set the cells size and margin
CELL_WIDTH = 15
CELL_HEIGHT = 15
CELL_MARGIN = 1

GAME_STATES = ['neutrall','setting_walls','searching']



# Classes
class Game(object):
    def __init__(self):
        self.grid = finder.map.grid

    def run_logic(self):
        pass

    def process_events(self):
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                return True  # Flag that we are exit so we exit this loop

    def display_frame(self, screen):
        screen.fill(BLUE)
        self.draw_grid(screen)

        # Update the screen with what we've drawn.
        pygame.display.flip()

    def draw_grid(self, screen):
        # Draw the grid
        for row in range(len(self.grid)):
            for column in range(len(self.grid)):
                color = GREEN
                if self.grid[row][column] == 1:
                    color = BROWN
                if self.grid[row][column] == 2:
                    color = GRAY
                pygame.draw.rect(screen,
                                color,
                                [(CELL_MARGIN + CELL_WIDTH) * column + CELL_MARGIN,
                                (CELL_MARGIN + CELL_HEIGHT) * row + CELL_MARGIN,
                                CELL_WIDTH,
                                CELL_HEIGHT])

class MapGrid(pathfinder.Map):
    def __init__(self, width=40, height=40):
        super().__init__(width=width, height=height)



def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
 
    # Set title of the game window
    pygame.display.set_caption("Pathfinder")
 
    # Create our objects and set the data
    done = False
    draw_walls = False
    clock = pygame.time.Clock()
 
    # Create an instance of the Game class
    game = Game()
 
    # Main game loop
    while not done:
 
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
 
        # Update object positions, check for collisions
        game.run_logic()
 
        # Draw the current frame
        game.display_frame(screen)
 
        # Pause for the next frame
        clock.tick(60)
 
    # Close window and exit
    pygame.quit()
    sys.exit()
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()
