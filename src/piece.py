import pygame
from settings.constants import SQUARE_SIZE

class Piece:
    def __init__(self, window) -> None:
        self.image = None
        self.name = ''
        self.color = 0

        self.window = window

        self.x = 0.0
        self.y = 0.0

    def draw(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.image = pygame.transform.scale(self.image,(SQUARE_SIZE, SQUARE_SIZE))
        self.window.blit(self.image, self.rect)

class King(Piece):
    def __init__(self, window) -> None:
        super().__init__(window)
        common_image = pygame.image.load('src/assets/pieces.png').convert_alpha()
        img_rect = pygame.Rect(0,0,300,300)
        self.image = pygame.Surface(img_rect.size)
        
    