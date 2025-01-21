from settings import *

class Game:
    def __init__(self):
        pass
        # General
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            # Allows you to close
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Shows the window indefinitely
            pygame.display.update()



if __name__ == '__main__':
    game = Game()
    game.run()
