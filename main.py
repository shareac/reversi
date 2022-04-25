# main file
from revsys import cui_game
import pygame
from settings import SCREEN_SIZE
from revgra import Tile

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    tiles = [Tile(x, y) for x in range(8) for y in range(8)]

    working = True
    while working:
        screen.fill((0, 0, 0))

        for tile in tiles: tile.draw(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: working = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for tile in tiles:
                    if event.pos in tile:
                        tile.set_color((255, 0, 0))
    pygame.quit()



if __name__ == "__main__":
    cui_game()
    # main()
