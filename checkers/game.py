import pygame
from .constants import *
from .board import *

class Game:
    def __init__(self, wind):
        self._init()
        self.wind = wind

    def update(self):
        self.board.draw(self.wind, self.valid_moves)
        if self.piece_sel == False:
            self.valid_moves = []
        pygame.display.update()

    def winner(self):
        if self.board.play1_left <= 0:
            return 'Player1'
        elif self.board.play2_left <= 0:
            return 'Player2'
        return None

    def _init(self):
        self.piece_sel = None
        self.board = Board()
        self.turn = PLAY2_COLOR
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.piece_sel:
            self.piece_sel.selected = False
            result = self._move(row, col)
            if not result:
                self.piece_sel = piece

        if piece != 0 and piece.color == self.turn:
            piece.selected = True
            self.piece_sel = piece
            self.valid_moves = self.get_valid_moves(piece)
            return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.piece_sel and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.piece_sel, row, col)
            skipped = self.valid_moves[(row,col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
            return True
        return False
   
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == PLAY1_COLOR or piece.king:
            moves.update(self._traverse(row + 1, ROWS, 1, piece.color, left, piece.king))
            moves.update(self._traverse(row + 1, ROWS, 1, piece.color, right, piece.king))

        if piece.color == PLAY2_COLOR or piece.king:
            moves.update(self._traverse(row - 1, -1, -1, piece.color, left, piece.king))
            moves.update(self._traverse(row - 1, -1, -1, piece.color, right, piece.king))
        
        return moves

    def _traverse(self, start, stop, step, color, direc, king, skipped=[]):
        moves = {}
        last = []
        for row in range(start, stop, step):
            if direc < 0 or direc >= COLS:
                break

            current = self.board.get_piece(row, direc)
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(row, direc)] = last + skipped
                else:
                    moves[(row, direc)] = last

                if last:
                    moves.update(self._traverse(row+step, stop, step, color, direc-1, king, skipped=last))
                    moves.update(self._traverse(row+step, stop, step, color, direc+1, king, skipped=last))
                if not king:
                    break

            elif current.color == color:
                break
            else:
                if last:
                    break
                last = [current]

            if direc < 0:
                direc -= 1 
            else:
                direc += 1
        return moves

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == PLAY1_COLOR:
            self.turn = PLAY2_COLOR
        else:
            self.turn = PLAY1_COLOR

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()
