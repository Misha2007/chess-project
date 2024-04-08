import pygame

from const import *

class Dragging():
    
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0
        
        #blit
        
        def update_blit(self, surface):
            # texture
            self.piece.set_texture(size=128)
            texture = self.piece.texture
            # img
            img = pygame.image.load(texture)
            # rect
            img_center = (self.mouseX, self.mouseY)
            self.piece.texture_rect = img.get_rect(center=img_center)
            # blit
            surface.blit(img, self.piece.texture_rect)
