from http import client
import raylib
from client.constants import *
from client.piece import *
from client.board import Board
from raylib.colors import *

"""
raylib [core] example - Basic window
"""
import pyray

# Initialization
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

pyray.init_window(WIDTH, HIGHT,'Chess')
pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second

img = pyray.load_image('src/assets/Pieces.png')
texture = pyray.load_texture_from_image(img)
board = Board(texture)
board.init_board()


# Main game loop
while not pyray.window_should_close():  # Detect window close button or ESC key
    # Update
    # TODO: Update your variables here
    if pyray.is_mouse_button_released(pyray.MOUSE_BUTTON_LEFT):
        pos = board.get_position(pyray.get_mouse_position())
        board.click(pos)

    # Draw
    pyray.begin_drawing()
    pyray.clear_background(BLACK)
    board.draw()
    pyray.draw_text('8', 4,50, 10, BLUE)
    pyray.end_drawing()


# De-Initialization
pyray.close_window()  # Close window and OpenGL context

