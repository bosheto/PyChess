import pygame
from piece import Piece
from settings.constants import SQUARE_SIZE, WIDTH, HIGHT, FPS
from board import Board
from sprite_sheet import SpriteSheet
WINDOW = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption('Chess')


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    filename = 'src/assets/pieces.png'
    ss = SpriteSheet(filename)
    king_rect = (0,0,668/2,int(2000/6))
    king_img = ss.image_at(king_rect, 0)
    king_piece = Piece(WINDOW)
    
    king_piece.image = king_img

    while(run):
        clock.tick(FPS)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_board(WINDOW)
        king_piece.x = SQUARE_SIZE
        king_piece.draw()
        pygame.display.update()

    pygame.quit()

main()
