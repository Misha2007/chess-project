import pygame
from const import *

class Game():
    def __init__(self):
        self.theme_light = (234, 235, 200)
        self.theme_dark = (119, 154, 88)
        self.current_theme = self.theme_light

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = self.theme_light
                else:
                    color = self.theme_dark
            
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

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
