import pygame
from const import *

def mainloop():
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption(caption)

    # Run until the user asks ti quit
    running = True
    while running:
        screen.fill(bg_color)
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Flip the display
        pygame.display.flip()


    # Done! Time to quit.
    pygame.quit()

mainloop()