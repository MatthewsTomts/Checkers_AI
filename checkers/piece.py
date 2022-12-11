from .constants import *
from pygame import draw

class Piece:
    def __init__(self, row, col, color, selected):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = self.y = 0
        self.calc_pos()
        self.selected = False

    def calc_pos(self):
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, wind):
        radius = SQUARE_SIZE // 2 - PADDING

        if self.selected:
            draw.circle(wind, SELECTED_COLOR, (self.x, self.y), radius + OUTLINE + SELECTED)

        # It defines the color of the outline
        if self.color == PLAY1_COLOR:
            out_color = OUTLINE_PLAY1
        else:
            out_color = OUTLINE_PLAY2

        # It draws the piece and the outline
        draw.circle(wind, out_color, (self.x, self.y), radius + OUTLINE)
        draw.circle(wind, self.color, (self.x, self.y), radius)

        if self.king:
            wind.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
