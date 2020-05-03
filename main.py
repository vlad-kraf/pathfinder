import pygame
from pathfinder import *

# Set colors
BLACK = (0, 0, 0) # background
GREEN = (27, 143, 23) # available for use cells
BROWN = (99, 43, 0) # path cells
GRAY = (107, 102, 97) # wall cells
 
# Set the margin between cells
WIDTH = 20
HEIGHT = 20
# Set the margin between each cell
MARGIN = 1
 

grid = graph.grid
 
pygame.init()
 
# Calculation of creen size
WINDOW_SIZE = [(len(grid)*WIDTH)+(len(grid)*MARGIN), (len(grid)*HEIGHT)+(len(grid)*MARGIN)]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Pathfinder")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# ain Program Loop
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(len(grid)):
        for column in range(len(grid)):
            color = GREEN
            if grid[row][column] == 1:
                color = BROWN
            if grid[row][column] == 2:
                color = GRAY
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()