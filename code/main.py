import pygame, sys
from const import *
from game import Game


class Main:
    """The main class in which game work."""

    def __init__(self):
        pygame.init()
        # Set up the drawing window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(caption)
        self.game = Game()

    def mainloop(self):
        # Run until the user asks ti quit
        running = True
        while running:
            self.game.show_bg(self.screen)
            self.game.show_moves(self.screen)
            self.game.show_pieces(self.screen)
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.game.change_theme(self
                                               .screen)

            # Flip the display
            pygame.display.flip()

main = Main()
main.mainloop()