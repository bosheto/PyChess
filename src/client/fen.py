from .piece import Piece

class FenString:

    pieces_dict = {
        'r' : Piece.Rook + Piece.Black,
        'n' : Piece.Knight + Piece.Black,
        'b' : Piece.Bishop + Piece.Black,
        'q' : Piece.Queen + Piece.Black,
        'k' : Piece.King + Piece.Black,
        'p' : Piece.Pawn + Piece.Black,
        'R' : Piece.Rook + Piece.White,
        'N' : Piece.Knight + Piece.White,
        'B' : Piece.Bishop + Piece.White,
        'Q' : Piece.Queen + Piece.White,
        'K' : Piece.King + Piece.White,
        'P' : Piece.Pawn + Piece.White,
    }

    @classmethod
    def read(self, fen_string):
        rank = 56
        file = 0
        board = [0 for x in range(64)]
        fen_string = fen_string
        for char in fen_string:
            if char.isdigit():
                file += int(char)
            elif char == '/':
                rank -= 8
                file = 0
            else:
                board[rank+file] = self.pieces_dict[char]
                file += 1

        return board

    @classmethod
    def create(self, board):
        file = 0
        rank = 56
        out_fen = ''
        in_empty_square = False
        empty_squares = 0
        for i in board:
            piece = board[rank+file]

            if piece != 0:
                if empty_squares > 0:
                    out_fen += str(empty_squares)
                    empty_squares = 0
                    in_empty_square = False
                out_fen += self.piece_from_id(piece)
            else:
                in_empty_square = True

            if in_empty_square:
                empty_squares += 1

            file += 1
            if file > 7:
                file = 0
                rank -= 8
                if empty_squares > 0:
                    out_fen += str(empty_squares)
                    empty_squares = 0
                    in_empty_square = False
                out_fen += '/'

        return out_fen[:-1]

    def piece_from_id(self, id):
        for item, val in self.pieces_dict.items():
            if val == id:
                return item
