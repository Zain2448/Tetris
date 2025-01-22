import pygame.draw

from settings import *

class Game:
    def __init__(self):
        # Main Surface
        self.display_surface = pygame.display.get_surface()

        # Game surface
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.rect = self.surface.get_rect(topleft=(0,0))

        # surface for the grid
        self.grid_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))

        # Color we are definitely not going to use
        self.grid_surface.fill((111,122,133))
        # This color is hidden/ignored
        self.grid_surface.set_colorkey((111,122,133))
        # Reduces transparency
        self.grid_surface.set_alpha(3)
        # now the can see the background color of the game surface
        self.surface.fill('#1C1C1C')


    def draw_grid(self):
        for col in range(1,COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.grid_surface,'#FFFFFF',(x,0),(x,self.surface.get_height()))

            for row in range(1,ROWS):
                y = row * CELL_SIZE
                pygame.draw.line(self.grid_surface,'#FFFFFF',(0,y),(self.surface.get_width(),y))

        # Places the grid surface on the game surface
        self.surface.blit(self.grid_surface, (0, 0))


    def run(self):
        # allows you to place one game surface onto the main surface. You also have to give the x and y coordinates
        self.draw_grid()
        self.display_surface.blit(self.surface, (PADDING, PADDING))
        pygame.draw.rect(self.surface, (255,255,255),self.rect,1)











