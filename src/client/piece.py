from pyray import Rectangle, draw_texture_rec, Vector2, load_image, load_texture_from_image
from raylib.colors import WHITE


# img = load_image('src/assets/Pieces.png')
# texture = load_texture_from_image(img)

class Piece:
    x = 0
    y = 0
    tile_x = 0
    color = 0
    name = 0
    texture = None
    id = 0

    King = 1
    Queen = 2
    Bishop = 3
    Knight = 4
    Rook = 5
    Pawn = 6

    White = 0
    Black = 10

    def draw(self, id, pos):
        self.color_id(id)
        rec = Rectangle(self.tile_x * 100 ,0 + (100*self.color),100,100)
        draw_texture_rec(self.texture, rec, Vector2(pos.x*100,pos.y*100), WHITE)

    def color_id(self, id):
        if id > 10:
            self.color = 1
        else:
            self.color = 0
        self.id = id % 10
        self.tile_x = self.id - 1
