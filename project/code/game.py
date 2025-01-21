import pygame.draw
from pygame.draw_py import draw_line

from settings import *

class Game:
    def __init__(self):

        # Game surface
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        # Main Window get_surface get the display surface, and it can be accessed anywhere
        self.display_surface = pygame.display.get_surface()


    def draw_grid(self):
        for col in range(1,COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.surface,'#FFFFFF',(x,0),(x,self.surface.get_height()))

            for row in range(1,ROWS):
                y = row * CELL_SIZE
                pygame.draw.line(self.surface,'#FFFFFF',(0,y),(self.surface.get_width(),y))


    def run(self):
        # allows you to place one game surface onto the main surface. You also have to give the x and y coordinates
        self.draw_grid()
        self.display_surface.blit(self.surface, (PADDING, PADDING))


