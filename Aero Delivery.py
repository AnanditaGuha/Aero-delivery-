import pygame
from pygame.locals import *

WINSIZE = [1024,768]
def main():
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    while True:
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                return

if __name__ == '__main__':
    main()

pygame.quit()
quit()
