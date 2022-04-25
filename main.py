# main file
# from revsys import cui_game
import pygame

from settings import SCREEN_SIZE, EDGE_COLOR, TILE_MAX
from revsys import System, Position
from revgra import Tile, Side

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("REVERSI")

    system = System()
    tiles = [ Tile(n) for n in range(TILE_MAX) ]
    side = Side()

    working = True

    while working:
        screen.fill(EDGE_COLOR)

        for n, tile in enumerate(tiles): tile.draw(screen, system.board.status(Position(n)))

        side.draw(screen, system)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: working = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for n, tile in enumerate(tiles):
                    if event.pos in tile:
                        system.put_stone(Position(n))

    pygame.quit()

if __name__ == "__main__":
    # cui_game()
    main()
