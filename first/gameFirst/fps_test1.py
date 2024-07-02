import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((640, 480))


def main():
    sysfont = pygame.font.SysFont(None, 48)
    counter = 0
    while True:
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

        counter += 1
        SURFACE.fill((0, 0, 0))
        count_image = sysfont.render("count is {}".format(counter), True, (255, 255, 255))
        SURFACE.blit(count_image, (50, 50))
        pygame.display.update()


if __name__ == '__main__':
    main()

