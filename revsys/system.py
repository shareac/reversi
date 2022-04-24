from .state import State
from .position import Position
from .board import Board
from .turn import Turn

class System:
    def __init__(self):
        self._board = Board()
        self._turn = Turn()
        self._game_status = 0

    def put_stone(self, p: Position):
        if self._board.is_puttable(p, self._turn.state):
            self._board.put_stone(p, self._turn.state)
            self._game_status = self._board.game_check()
            self._turn.next(self._game_status)
        else:
            print(f"({p.x}, {p.y}) には置けない!")

    def can_next(self):
        return self._game_status < 5

    def prints(self):
        self._board.prints()
        self._turn.prints()

    @property
    def game_status(self):
        return self._game_status
