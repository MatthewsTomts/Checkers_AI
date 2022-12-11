from copy import deepcopy
import pygame


PLAY1_COLOR = (0, 0, 210)
PLAY2_COLOR = (210, 0, 0)

def minimax(position, depth, player, game):
    if depth == 0 or game.winner() != None:
        return evaluate(position), position

    if player == PLAY2_COLOR:
        maxEval = float('-inf')
        best_move = position
        for move in get_all_moves(position, player, game):
            evaluation = minimax(move, depth-1, player, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('+inf')
        best_move = position
        for move in get_all_moves(position, player, game):
            evaluation = minimax(move, depth-1, player, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move

def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = game.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            #draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(200)

def evaluate(position):
    return position.play1_left - position.play2_left + (position.play1_kings * 0.5 + position.play2_kings * 0.5)
