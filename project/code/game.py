from settings import *

class Game:
    def __init__(self):

        # Game surface
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        # Main Window get_surface get the display surface, and it can be accessed anywhere
        self.display_surface = pygame.display.get_surface()

    def run(self):
        # allows you to place one game surface onto the main surface. You also have to give the x and y coordinates
        self.display_surface.blit(self.surface, (PADDING, PADDING))




        pass