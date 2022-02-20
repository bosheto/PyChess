from curses import window
import pygame
from settings.constants import WIDTH, HIGHT, FPS
from ..board import Board
WINDOW = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption('Chess')


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    while(run):
        clock.tick(FPS)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_board(window)

    pygame.quit()
