import pygame
from checkers import WIDTH, HEIGHT, SQUARE_SIZE, PLAY1_COLOR, PLAY2_COLOR
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

# Define the size of the window
WIND = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers') # Window Title

def get_x_y_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIND)

    while run:
        # Set the loop to run in a determined time in this case is 60fps
        clock.tick(FPS)
        game.update()

        if game.winner() != None:
            print(game.winner())
            run = False

        if game.turn == PLAY1_COLOR:
            new_board = minimax(game.get_board(), 3, PLAY1_COLOR, game)[1]
            game.ai_move(new_board)
        if game.turn == PLAY2_COLOR:
            new_board = minimax(game.get_board(), 3, PLAY2_COLOR, game)[1]
            game.ai_move(new_board)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_x_y_mouse(pos)
                game.select(row, col)
            
    pygame.quit()

main()
