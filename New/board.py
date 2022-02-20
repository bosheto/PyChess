from piece import piece_dict, Piece
from pyray import draw_rectangle
from raylib.colors import (
    RAYWHITE,
    LIGHTGRAY,
    WHITE,
    BLACK,
    DARKGRAY
)


class Board:

    turn = 0
    selected_piece = None

    def __init__(self, texture):
        self.board = [[0 for y in range(8)] for x in range(8)]
        self.selected_piece = None
        self.white_pieces = None
        self.black_pieces = None
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
        for x in range(8):
            for y in range(8):
                id = self.board[x][y]
                if id != 0:
                    self.piece.draw(id, Position(x, y))

    def add(self, piece, pos):
        self.board[pos.x][pos.y] = piece

    # FIXME this will be affected
    def select_piece(self, pos):
        piece = self.board[pos.x][pos.y]
        if piece:
            self.selected_piece = self.board[pos.x][pos.y]

    # FIXME this will be affected
    def move(self, ex, ey):
        piece = self.selected_piece
        self.board[piece.x][piece.y] = None
        piece.move(ex, ey)
        self.add(piece)

    def click(self, pos):
        if self.selected_piece:
            self.move(pos.x, pos.y)
            self.selected_piece = None
            return
        else:
            self.select_piece(pos)
            return

    def get_position(self, pos):
        pos.x = int((pos.x / 100) - (pos.x / 100) % 1)
        pos.y = int((pos.y / 100) - (pos.y / 100) % 1)
        return self._board_position(pos)

    def _board_position(self, vec2):
        x = int(vec2.x)
        y = int(vec2.y)
        return Position(x, y)

    @DeprecationWarning
    def get_piece_from_id(self, id):
        if id >= 1 and id < 7:
            return piece_dict[id]
        return None


class Position:

    reference_positions = {'a1': {'x': 0, 'y': 0},
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
        return '?'

class FenString:
    # initial position: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR

    def read_string(self, fen_string):
        pass

Position.to_flat(Position(0,0))