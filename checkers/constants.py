from pygame import image, transform

# Window Size
WIDTH = HEIGHT = 700
ROWS = COLS = 8
SQUARE_SIZE = WIDTH//COLS

# the crown image
CROWN = transform.scale(image.load('checkers/assets/crown.png'), (445 * (SQUARE_SIZE / 800), 256 * (SQUARE_SIZE / 800)))

# Pieces constants
PADDING = 13
OUTLINE = 2
SELECTED = 3

# RGB colors of the objects

# Blue
PLAY1_COLOR = (0, 0, 210)

# Black
OUTLINE_PLAY1 = (255, 255, 255)

# Red
PLAY2_COLOR = (210, 0, 0)

# White
OUTLINE_PLAY2 = (255, 255, 255) 

# Green
SELECTED_COLOR = (0, 220, 0)

# Black
BOARD_SQUARE1 = (205, 205, 205)

# Black
BOARD_SQUARE2 = (10, 10, 10)

# Green
MOVE_COLOR = (0, 255, 0)
