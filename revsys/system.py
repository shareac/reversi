from .state import State
from .position import Position
from .board import Board
from .turn import Turn

class System:
    def __init__(self):
        self.board = Board()
        self.turn = Turn()
        self._game_status = 0

    def put_stone(self, p: Position):
        if self.board.is_puttable(p, self.turn.state):
            self.board.put_stone(p, self.turn.state)
            self._game_status = self.board.game_check()
            self.turn.next(self._game_status)
        else:
            print(f"({p.x}, {p.y}) には置けない!")

    def can_next(self):
        return self._game_status < 5

    def prints(self):
        self.board.prints()
        self.turn.prints()

    @property
    def game_status(self):
        return self._game_status
