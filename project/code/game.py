import random
import pygame.time
from settings import *
from timer import Timer

class Game:
    def __init__(self):
        # Main Surface
        self.display_surface = pygame.display.get_surface()

        # Game surface
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.rect = self.surface.get_rect(topleft=(PADDING,PADDING))

        # surface for the grid
        self.grid_surface = self.surface.copy()

        # Color we are definitely not going to use
        self.grid_surface.fill((111,122,133))
        # This color is hidden/ignored
        self.grid_surface.set_colorkey((111,122,133))
        # Reduces transparency
        self.grid_surface.set_alpha(45)


        # Creating the sprites
        self.sprites = pygame.sprite.Group()
        self.tetromino = Tetrominos(random.choice(list(TETROMINOS.keys())),self.sprites)

        # timer
        self.timers = {
            'vertical_move': Timer(UPDATE_TIMER,True,self.move_down),
            # timer is need so when the key is pressed once it is moved once
            'horizontal_move': Timer(MOVE_WAIT_TIME)
        }
        self.timers['vertical_move'].activate()

    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def move_down(self):
        self.tetromino.move_down()

    def draw_grid(self):
        for col in range(1,COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.grid_surface,'#FFFFFF',(x,0),(x,self.surface.get_height()))

        for row in range(1,ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.grid_surface,'#FFFFFF',(0,y),(self.surface.get_width(),y))

        # Places the grid surface on the game surface
        self.surface.blit(self.grid_surface, (0, 0))

    def user_input(self):
        # contains all the possible user inputs
        keys = pygame.key.get_pressed()

        if not self.timers['horizontal_move'].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.move_horizontal(-1)
                # now the timer is activated so the user cant press the button for 120 ms
                self.timers['horizontal_move'].activate()
            if keys[pygame.K_RIGHT]:
                self.tetromino.move_horizontal(1)
                self.timers['horizontal_move'].activate()

    def run(self):
        # allows you to place one game surface onto the main surface. You also have to give the x and y coordinates
        self.display_surface.blit(self.surface, (PADDING, PADDING))

        self.surface.fill('#1C1C1C')
        self.draw_grid()
        pygame.draw.rect(self.display_surface, (255,255,255),self.rect,2,2)

        # Places the sprite on the surface
        self.sprites.draw(self.surface)
        # Update timer and Sprite. These method are called continuously (i.e. frame by frame)
        self.timer_update()
        self.sprites.update()

        self.user_input()




class Block(pygame.sprite.Sprite):
    def __init__(self, group, color, pos):
        # Sprites are place in a group. This group will update/move the sprite
        super().__init__(group)
        # Makes a surface that takes up exactly one block
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)

        # position
        self.pos = pygame.math.Vector2(pos)
        x = self.pos.x * CELL_SIZE
        y = self.pos.y * CELL_SIZE
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self):
        x = self.pos.x * CELL_SIZE
        y = self.pos.y * CELL_SIZE
        self.rect = self.image.get_rect(topleft=(x, y))


class Tetrominos:
    def __init__(self, shape, group):
        self.block_positions = TETROMINOS[shape]['positions']
        self.color = TETROMINOS[shape]['color']
        self.group = group
        # creates a list of blocks objects
        self.blocks = [Block(self.group, self.color, pos) for pos in self.block_positions]

    def move_down(self):
        for block in self.blocks:
            # Block is moved down by 1
            block.pos.y += 1

    def move_horizontal(self, move_by):
        for block in self.blocks:
            block.pos.x += move_by


