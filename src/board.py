from math import sqrt
import pygame
from settings.constants import *

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.white_pieces = None
        self.black_pieces = None

    def draw_board(self, window):
        window.fill(BLACK)

        for file in range(FILE):
            for rank in range(RANK):
                
                colour = WHITE if (file + rank) % 2 == 0 else BLACK 
                pygame.draw.rect(window, colour, (file*SQUARE_SIZE, rank*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))