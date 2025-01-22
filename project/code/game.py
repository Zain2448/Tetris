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
        for col in range(COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.surface,'#FFFFFF',(x,0),(x,self.surface.get_height()))

            for row in range(ROWS):
                y = row * CELL_SIZE
                pygame.draw.line(self.surface,'#FFFFFF',(0,y),(self.surface.get_width(),y))

        # Outline
        pygame.draw.line(self.surface, '#FFFFFF', (GAME_WIDTH, 0), (GAME_WIDTH, GAME_HEIGHT), 3)
        pygame.draw.line(self.surface, '#FFFFFF', (0, GAME_HEIGHT), (GAME_WIDTH, GAME_HEIGHT), 3)


    def run(self):
        # allows you to place one game surface onto the main surface. You also have to give the x and y coordinates
        self.draw_grid()
        self.display_surface.blit(self.surface, (PADDING, PADDING))

class Block(pygame.sprite.Sprite):
    def __init__(self, group):
        # surface we want to display
        # any sprite you want to create is placed in a group.
        # This group will display and update the sprite. this will allow it to move
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.display_surface = pygame.display.get_surface()
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=(PADDING, PADDING))

    def run(self):
        self.display_surface.blit(self.image, (PADDING, PADDING))






