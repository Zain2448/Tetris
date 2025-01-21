from settings import *

class Score:
    def __init__(self):
        self.score = 0
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT*SCORE_HEIGHT_FRACTION - PADDING))
        self.display_surface = pygame.display.get_surface()
        # Makes it easier for you to place the panels
        self.rect = self.surface.get_rect(bottomright=(WINDOW_WIDTH-PADDING, WINDOW_HEIGHT - PADDING ))


    def run(self):
        # The panel is place based by the bottom right corner
        self.display_surface.blit(self.surface, self.rect)
