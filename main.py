# main file
# from revsys import cui_game
import pygame

from settings import SCREEN_SIZE, LINE_COLOR, TILE_MAX, WIDTH
from revsys import System, Position
from revgra import Tile

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    s = System()
    tiles = [ Tile(n) for n in range(TILE_MAX) ]

    working = True
    while working:
        screen.fill(LINE_COLOR)
        for n, tile in enumerate(tiles):
            x = n % WIDTH
            y = n // WIDTH
            tile.draw(screen, s.board.status(Position(x, y)))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: working = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for tile in tiles:
                    if event.pos in tile:
                        tile.set_color((255, 0, 0))
    pygame.quit()


if __name__ == "__main__":
    # cui_game()
    main()
