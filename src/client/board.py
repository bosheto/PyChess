from .piece import Piece
from pyray import draw_rectangle
from .fen import FenString
from raylib.colors import (
    LIGHTGRAY,
    DARKGRAY
)

class Board:

    player = 0

    selected_piece = None
    selected_square = None

    def __init__(self, texture):
        self.board = [0 for x in range(64)]
        self.texture = texture
        self.piece = Piece()
        self.piece.texture = self.texture

    def draw(self):
        self.draw_board()
        self.draw_pieces()

    def draw_board(self):
        for x in range(80):
            for y in range(80):
                colour = LIGHTGRAY if (x+y) % 2 == 0 else DARKGRAY
                draw_rectangle(x*100, y*100, 100, 100, colour)

    def draw_pieces(self):
        for index in range(len(self.board)):
            if self.board[index] != 0:
                self.piece.draw(self.board[index], Position.from_flat(index))

    def add(self, piece, pos):
        self.board[Position.to_flat(pos)] = piece

    def move(self, pos):
        if pos == self.selected_square:
            return
        piece = self.selected_piece
        self.board[self.selected_square] = 0
        self.board[pos] = piece
        self.selected_piece = None
        self.selected_square = None
        self.next_player()

    def click(self, pos):
        position = Position.to_flat(pos)
        if self.selected_piece is None:
            if self.check_colour(self.board[position]):
                self.selected_piece = self.board[position]
                self.selected_square = position
        else:
            self.move(position)

    def init_board(self, \
            fen_string = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'):
        self.board = FenString.read(fen_string)

    def get_position(self, pos):
        pos.x = int((pos.x / 100) - (pos.x / 100) % 1)
        pos.y = int((pos.y / 100) - (pos.y / 100) % 1)
        return self._board_position(pos)

    def _board_position(self, vec2):
        x = int(vec2.x)
        y = int(vec2.y)
        return Position(x, y)

    def check_colour(self, id):
        color = self.player_colour(id)
        if color == self.player:
            return True
        return False

    def player_colour(self, id):
        if id > 10: #BLACK
            piece_colour = 1
        else: # WHHITE
            piece_colour = 0
        return piece_colour

    def next_player(self):
        if self.player == 1:
            self.player = 0
        else:
            self.player = 1

class Position:

    reference_positions ={
        'a1': {'x': 0, 'y': 0},
        'a2': {'x': 0, 'y': 1},
        'a3': {'x': 0, 'y': 2},
        'a4': {'x': 0, 'y': 3},
        'a5': {'x': 0, 'y': 4},
        'a6': {'x': 0, 'y': 5},
        'a7': {'x': 0, 'y': 6},
        'a8': {'x': 0, 'y': 7},
        'b1': {'x': 1, 'y': 0},
        'b2': {'x': 1, 'y': 1},
        'b3': {'x': 1, 'y': 2},
        'b4': {'x': 1, 'y': 3},
        'b5': {'x': 1, 'y': 4},
        'b6': {'x': 1, 'y': 5},
        'b7': {'x': 1, 'y': 6},
        'b8': {'x': 1, 'y': 7},
        'c1': {'x': 2, 'y': 0},
        'c2': {'x': 2, 'y': 1},
        'c3': {'x': 2, 'y': 2},
        'c4': {'x': 2, 'y': 3},
        'c5': {'x': 2, 'y': 4},
        'c6': {'x': 2, 'y': 5},
        'c7': {'x': 2, 'y': 6},
        'c8': {'x': 2, 'y': 7},
        'd1': {'x': 3, 'y': 0},
        'd2': {'x': 3, 'y': 1},
        'd3': {'x': 3, 'y': 2},
        'd4': {'x': 3, 'y': 3},
        'd5': {'x': 3, 'y': 4},
        'd6': {'x': 3, 'y': 5},
        'd7': {'x': 3, 'y': 6},
        'd8': {'x': 3, 'y': 7},
        'e1': {'x': 4, 'y': 0},
        'e2': {'x': 4, 'y': 1},
        'e3': {'x': 4, 'y': 2},
        'e4': {'x': 4, 'y': 3},
        'e5': {'x': 4, 'y': 4},
        'e6': {'x': 4, 'y': 5},
        'e7': {'x': 4, 'y': 6},
        'e8': {'x': 4, 'y': 7},
        'f1': {'x': 5, 'y': 0},
        'f2': {'x': 5, 'y': 1},
        'f3': {'x': 5, 'y': 2},
        'f4': {'x': 5, 'y': 3},
        'f5': {'x': 5, 'y': 4},
        'f6': {'x': 5, 'y': 5},
        'f7': {'x': 5, 'y': 6},
        'f8': {'x': 5, 'y': 7},
        'g1': {'x': 6, 'y': 0},
        'g2': {'x': 6, 'y': 1},
        'g3': {'x': 6, 'y': 2},
        'g4': {'x': 6, 'y': 3},
        'g5': {'x': 6, 'y': 4},
        'g6': {'x': 6, 'y': 5},
        'g7': {'x': 6, 'y': 6},
        'g8': {'x': 6, 'y': 7},
        'h1': {'x': 7, 'y': 0},
        'h2': {'x': 7, 'y': 1},
        'h3': {'x': 7, 'y': 2},
        'h4': {'x': 7, 'y': 3},
        'h5': {'x': 7, 'y': 4},
        'h6': {'x': 7, 'y': 5},
        'h7': {'x': 7, 'y': 6},
        'h8': {'x': 7, 'y': 7}}

    def __init__(self, x, y) -> None:
            self.x = x
            self.y = y

    @classmethod
    def to_flat(self, pos):
        return 56 - (pos.y * 8) + pos.x

    @classmethod
    def from_notation(cls, notation):
        pos = cls.reference_positions[notation.lower()]

        return Position(pos['x'], 7 - pos['y'])

    @classmethod
    def from_flat(cls, pos):
        if pos == 0:
            return Position.from_notation('a1')

        y = 7 - int(pos / 8)
        x = pos - (int(pos/8) * 8)

        return Position(x,y)
