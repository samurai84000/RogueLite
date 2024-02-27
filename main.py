import sys
import level
import pygame
from randomcode import *

Width, Height = 1280, 720
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Width, Height))
        pygame.display.set_caption("Roguelite")
        self.level1 = level.Level()
        self.clock = pygame.time.Clock()
        self.run()
        pygame.mouse.set_visible(False)



    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('black')
            self.level1.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
