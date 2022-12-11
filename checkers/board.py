from pygame import draw
from .constants import *
from .piece import *

class Board:
    def __init__(self):
        self.board = []
        self.play1_left = self.play2_left = 12
        self.play1_kings = self.play2_kings = 0
        self.create_board()

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def draw(self, wind, moves):
        self.draw_squares(wind)
        self.draw_valid_moves(wind, moves)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(wind)

    # Draw dots on the possibles moves
    def draw_valid_moves(self, wind, moves):
        for move in moves:
            row, col = move
            draw.circle(wind, MOVE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 7)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == PLAY1_COLOR:
                    self.play1_left -= 1
                else:
                    self.play2_left -= 1

    # Draw the board
    def draw_squares(self, wind):
        # fill the entire window with red
        wind.fill(BOARD_SQUARE2)
        for row in range(ROWS):
            # it will get the columns that it should draw the squares in each row
            # if it is the row 0, 0 % 2 == 0, so in the column 0 it will have a red square and just go om
            # increasing by two in that row
            for col in range(row % 2, ROWS, 2):
                draw.rect(wind, BOARD_SQUARE1, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == (row + 1) % 2:
                    if row < 3:
                        self.board[row].append(Piece(row, col, PLAY1_COLOR, False))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, PLAY2_COLOR, False))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def move(self, piece, row, col):
        # switch the piece and the empty space (0)
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        
        if (row == ROWS - 1 or row == 0) and not piece.king:
            piece.make_king()
            if piece.color == PLAY1_COLOR:
                self.play1_left += 1
            else:
                self.play2_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]
