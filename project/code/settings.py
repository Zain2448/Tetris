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
    'O': {'positions':[(1,0),(1,1),(2,0),(2,1)], 'color':'blue'},
    'L': {'positions':[(3,0),(3,1),(3,2),(4,2)], 'color':'green'},
    'Z': {'positions':[(4,0),(5,0),(5,1),(6,1)], 'color':'yellow'},
    'S': {'positions':[(7,1),(8,1),(8,0),(9,0)], 'color':'cyan'},
    'T': {'positions':[(0,9),(1,9),(2,9),(1,10)], 'color':'magenta'},
    'J': {'positions':[(5,7),(5,8),(5,9),(4,9)], 'color':'orange'},
}

UPDATE_TIMER = 1000
MOVE_WAIT_TIME = 120



