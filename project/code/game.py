import pygame.draw
from settings import *

class Game:
    def __init__(self):
        # Main Surface
        self.display_surface = pygame.display.get_surface()

        # Game surface
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.rect = self.surface.get_rect(topleft=(PADDING,PADDING))

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

        # Creating the sprites
        self.sprites = pygame.sprite.Group()

        for key in TETROMINOS:
            for i in range(0, 4):
                color = TETROMINOS[key]['color']
                x = TETROMINOS[key]['positions'][i][0]
                y = TETROMINOS[key]['positions'][i][1]
                self.block = Block(self.sprites, color, x, y)


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
        self.display_surface.blit(self.surface, (PADDING, PADDING))

        self.draw_grid()
        pygame.draw.rect(self.display_surface, (255,255,255),self.rect,2,2)

        # Places the sprite on the surface
        self.sprites.draw(self.surface)

class Block(pygame.sprite.Sprite):
    def __init__(self, group, color, col, row):
        # Sprites are place in a group. This group will update/move the sprite
        super().__init__(group)
        # Makes a surface that takes up exactly one block
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)

        # position
        x = col * CELL_SIZE
        y = row * CELL_SIZE
        self.rect = self.image.get_rect(topleft=(x,y))

