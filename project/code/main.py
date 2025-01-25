from settings import *

# Component
from game import Game
from score import Score
from preview import Preview

class Main:
    def __init__(self):
        pass
        # General
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tetris")

        # Components
        self.game = Game()
        self.score = Score()
        self.preview = Preview()



    def run(self):
        while True:
            # Allows you to close
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Shows the window indefinitely
            pygame.display.update()
            # Sets frames per second
            self.clock.tick()
            # Background color
            self.display_surface.fill('#222222')


            # Components
            self.game.run()
            self.score.run()
            self.preview.run()


if __name__ == '__main__':
    main = Main()
    main.run()
