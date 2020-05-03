import pygame
from pathfinder import *

# Set colors
BLACK = (0, 0, 0) # background
GREEN = (144, 190, 109) # available for use cells
BROWN = (154, 140, 152) # path cells
GRAY = (87, 117, 144) # wall cells
BLUE = (224, 251, 252)

 
# Set the margin between cells
WIDTH = 15
HEIGHT = 15
# Set the margin between each cell
MARGIN = 1
 

grid = finder.map.grid

pygame.init()
 
# Calculation of creen size
#WINDOW_SIZE = [(len(grid)*WIDTH)+(len(grid)*MARGIN), (len(grid)*HEIGHT)+(len(grid)*MARGIN)]
WINDOW_SIZE = [800, 640]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Pathfinder")
 
# Loop until the user clicks the close button.
exit = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

draw_walls = 0
# Main Program Loop
while not exit:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            exit = True  # Flag that we are exit so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            draw_walls = 1
            pos = pygame.mouse.get_pos()
            x, y = pos[1] // (HEIGHT + MARGIN), pos[0] // (WIDTH + MARGIN)
            grid[x][y] = 2
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            draw_walls = 0
        elif event.type == pygame.MOUSEMOTION and draw_walls == 1:
            pos = pygame.mouse.get_pos()
            x, y = pos[1] // (HEIGHT + MARGIN), pos[0] // (WIDTH + MARGIN)
            grid[x][y] = 2
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            pos = pygame.mouse.get_pos()
            x, y = pos[1] // (HEIGHT + MARGIN), pos[0] // (WIDTH + MARGIN)
            grid[x][y] = 0


        

 
    # Set the screen background
    screen.fill(BLUE)
 
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