import sys
from .state import State

class Turn:
    def __init__(self):
        self._turn = State.BLACK

    def change(self):
        if self._turn == State.WHITE:
            self._turn = State.BLACK
        elif self._turn == State.BLACK:
            self._turn = State.WHITE

    def __repr__(self):
        if self._turn == State.BLACK:
            return "黑"
        if self._turn == State.WHITE:
            return "白"
        return "なし"

    """
    game check code:
      0 : when both players can put a stone somewhere legally
      1 : when WHITE cannot put a stone but BLACK can
     -1 : when BLACK cannot put a stone but WHITE can
     10 : when DRAW
     11 : when BLACK wins
      9 : when WHITE wins
    """
    def next(self, game_status):
        if game_status == 0:
            self.change(); return
        if game_status == 1:
            self._turn = State.BLACK; return
        if game_status == -1:
            self._turn = State.WHITE; return
        if game_status in [9, 10, 11]:
            self._turn = game_status; return
        print("ここには来ない @ Turn")
        sys.exit()

    def is_state(self, state: State):
        return self._turn == state

    def prints(self):
        if self._turn == State.WHITE:
            print("白の番です"); return
        if self._turn == State.BLACK:
            print("黒の番です"); return
        if self._turn == 9:
            print("白の勝ち"); return
        if self._turn == 10:
            print("引き分け"); return
        if self._turn == 11:
            print("黒の勝ち"); return

    def clone(self):
        t = Turn()
        t._turn = self._turn
        return t

    @property
    def state(self):
        return self._turn
