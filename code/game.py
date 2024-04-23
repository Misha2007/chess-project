import pygame
from const import *
from board import Board
from dragging import Dragging
from square import Square

class Game():
    def __init__(self):
        self.board = Board()
        self.theme_light = (234, 235, 200)
        self.theme_dark = (119, 154, 88)
        self.current_theme = self.theme_light

    def show_bg(self, surface):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
        frame = (0, 0, WIDTH, HEIGHT)
        color_frame = self.theme_light
        # blit frame
        pygame.draw.rect(surface, color_frame, frame)
        frame2 = (19, 19, WIDTH - 38, HEIGHT- 38)
        # blit frame
        pygame.draw.rect(surface, (0,0,0), frame2)
        for row in range(ROWS):
            # add numbers
            number = row + 1
            my_font = pygame.font.SysFont('Comic Sans MS', 30)
            text_surface = my_font.render(str(number), False, self.theme_dark)
            surface.blit(text_surface, (5, row * SQSIZE + 60))
            for col in range(COLS):
                # add letters
                character = alphabet[col]
                my_font = pygame.font.SysFont('Comic Sans MS', 30)
                text_surface2 = my_font.render(character, False, self.theme_dark)
                surface.blit(text_surface2, (col * SQSIZE + 65, HEIGHT - 20))

                if (row + col) % 2 == 0:
                    color = self.theme_light
                else:
                    color = self.theme_dark
            
                rect = (col * SQSIZE + 20, row * SQSIZE + 20, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

    def change_theme(self, surface):
        # Get the keys (theme_light values) of the themes dictionary
        theme_light_keys = list(themes.keys())
    
        # Get the index of the current theme_light in the list of keys
        current_index = theme_light_keys.index(self.theme_light)
    
        # Calculate the index of the next theme_light, looping back to the start if necessary
        next_index = (current_index + 1) % len(themes)
    
        # Update the current theme_light and theme_dark to the next ones
        self.theme_light = theme_light_keys[next_index]
        self.theme_dark = themes[self.theme_light]

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture)
                    img_center = col * SQSIZE + SQSIZE // 2 + 20, row * SQSIZE + SQSIZE // 2 + 20
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)