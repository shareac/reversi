import pygame
from revsys import State
from .button import Button
from settings import *

class Tile(Button):
    def __init__(self, n):
        bx = (n % WIDTH) * (TILE_WIDTH + TILE_MARGIN * 2) + TILE_MARGIN
        by = (n // WIDTH) * (TILE_WIDTH + TILE_MARGIN * 2) + TILE_MARGIN
        super().__init__(bx, by, TILE_WIDTH, TILE_HEIGHT, TILE_COLOR)

    def draw(self, screen, state: State):
        super().draw(screen)
        if state == State.BLACK: pygame.draw.circle(screen, BLACK_COLOR, self.get_center(), STONE_RADIUS)
        if state == State.WHITE: pygame.draw.circle(screen, WHITE_COLOR, self.get_center(), STONE_RADIUS)
