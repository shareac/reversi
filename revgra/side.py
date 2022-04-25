import pygame
from settings import *
from revsys import State
from .button import Button

class Side(Button):
    def __init__(self):
        super().__init__(TILE_SIZE*WIDTH, 0, TILE_SIZE*2, TILE_SIZE*HEIGHT, SIDE_COLOR)
        self._blacks = BlackStone()
        self._whites = WhiteStone()
        self._info = Info()

    def draw(self, screen, system):
        super().draw(screen)
        self._blacks.draw(screen, system)
        self._whites.draw(screen, system)
        self._info.draw(screen, system)

class Info(Button):
    def __init__(self):
        super().__init__(TILE_SIZE*WIDTH+10, TILE_SIZE*2, TILE_SIZE*2-20, TILE_SIZE)
        self.set_color(INFO_COLOR)
        self.set_active(False)
        self.set_text("WHITE's Turn")
        self.set_textSize(TILE_SIZE*4//10)

    def draw(self, screen, system):
        if system.game_status in [-1, 0, 1]:
            if system.turn.state == State.WHITE:
                self.set_color(WHITE_COLOR)
                self.set_textColor(BLACK_COLOR)
                self.change_text("turn WHITE")
            elif system.turn.state == State.BLACK:
                self.set_color(BLACK_COLOR)
                self.set_textColor(WHITE_COLOR)
                self.change_text("turn BLACK")
        else:
            self.set_textColor(RED_COLOR)
            if system.turn.state == 10:
                self.set_color(DRAW_COLOR)
                self.change_text("DRAW")
            elif system.turn.state == 11:
                self.set_color(BLACK_COLOR)
                self.change_text("BLACK wins")
            elif system.turn.state == 9:
                self.set_color(WHITE_COLOR)
                self.change_text("WHITE wins")
            else:
                self.change_text("Unknown Error")

        super().draw(screen)

class Stone(Button):
    def __init__(self, y):
        super().__init__(TILE_SIZE*WIDTH, y, TILE_SIZE*2, TILE_SIZE*2)
        self.set_active(False)
        self.set_bg_visible(False)
        self.set_text("2")
        self.set_textSize(COUNT_SIZE)

class BlackStone(Stone):
    def __init__(self):
        super().__init__(0)
        self.set_textColor(WHITE_COLOR)

    def draw(self, screen, system):
        pygame.draw.circle(screen, BLACK_COLOR, self.get_center(), STONE_RADIUS*2)
        self.change_text(str(system.board.blacks))
        super().draw(screen)

class WhiteStone(Stone):
    def __init__(self):
        super().__init__(TILE_SIZE*3)

    def draw(self, screen, system):
        pygame.draw.circle(screen, WHITE_COLOR, self.get_center(), STONE_RADIUS*2)
        self.change_text(str(system.board.whites))
        super().draw(screen)
