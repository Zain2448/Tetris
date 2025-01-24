import pygame

# Game Size
COLUMNS = 10
ROWS = 20
CELL_SIZE = 30
GAME_WIDTH = COLUMNS * CELL_SIZE
GAME_HEIGHT = ROWS * CELL_SIZE


# Sidebar size
SIDEBAR_WIDTH = 200
# Takes 70 percent of sidebar
PREVIEW_HEIGHT_FRACTION = 0.7
# Takes 30 percent of sidebar
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION


# Window size
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2


# Tetromino - nested dictionary
TETROMINOS = {
    'I': {'positions':[(0,0),(0,1),(0,2),(0,3)], 'color':'red'},
    'O': {'positions':[(3,4),(3,5),(4,4),(4,5)], 'color':'blue'}
}



