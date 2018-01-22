"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame

PI = 3.14159265359
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 127, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (148, 0, 211)
SKY = (3, 255, 242)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 600)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Pretty Picture")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(SKY)
 
    # --- Drawing code should go here
    # Draw an arc as part of an ellipse. Use radians to determine what
    # angle to draw.
    pygame.draw.arc(screen, VIOLET, [123,90,460,490],   0,  PI, 5)
    pygame.draw.arc(screen, VIOLET, [123,90,460,490],   PI,  0, 5) 
    pygame.draw.arc(screen, INDIGO, [113,83,480,500],   0,  PI, 5)
    pygame.draw.arc(screen, INDIGO, [113,83,480,500],   PI,  0, 5)
    pygame.draw.arc(screen, BLUE,   [103,76,500,510],   0,  PI, 5)
    pygame.draw.arc(screen, BLUE,   [103,76,500,510],   PI,  0, 5)
    pygame.draw.arc(screen, GREEN,  [93,69,520,520],   0,   PI, 5)
    pygame.draw.arc(screen, GREEN,  [93,69,520,520],   PI,   0, 5)
    pygame.draw.arc(screen, YELLOW, [83,62,540,530],   0,   PI, 5)
    pygame.draw.arc(screen, YELLOW, [83,62,540,530],   PI,   0, 5)
    pygame.draw.arc(screen, ORANGE, [73,57,560,540],   0,   PI, 5)
    pygame.draw.arc(screen, ORANGE, [73,57,560,540],   PI,   0, 5)
    pygame.draw.arc(screen, RED,    [63,50,580,550],   0,   PI, 5)
    pygame.draw.arc(screen, RED,    [63,50,580,550],   PI,   0, 5)
  

    #pygame.draw.arc(screen, BLUE,   [100,55,530,430],   0,   PI, 7)
    #pygame.draw.arc(screen, INDIGO, [110,55,525,425],   0,   PI, 6)
    #pygame.draw.arc(screen, VIOLET, [120,55,520,420],   0,   PI, 5)       
        
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()