from .state import State
from .position import Position

class BoardBase():
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._board = [ [ State.EMPTY for j in range(width)] for i in range(height) ]
        self._whites = 0
        self._blacks = 0
        self._empties = self._width * self._height
        self._is_updated = False

    def set_state(self, p: Position, s: State):
        self._board[p.y][p.x] = s
        self._is_updated = False

    def is_state(self, p: Position, s: State):
        return self._board[p.y][p.x] == s

    # update how many stones are white/black/empty
    def _update(self):
        self._whites = self._blacks = self._empties = 0
        for array in self._board:
            for state in array:
                if state == State.EMPTY: self._empties += 1
                elif state == State.BLACK: self._blacks += 1
                elif state == State.WHITE: self._whites += 1

        self._is_updated = True
        if self._whites + self._blacks + self._empties == self._width * self._height: return  # normal

        print("wrong value(s) in the board.")
        self.prints()
        self._is_updated = False

    def prints(self):
        def printf(string): print(string, end="")
        for i, array in enumerate(self._board):
            printf(i)
            for state in array:
                if state == State.EMPTY: printf(" _")
                elif state == State.BLACK: printf(" x")
                elif state == State.WHITE: printf(" o")
                else: print(f"Error, not {state}")
            print("")
        printf("/")
        for i in range(self._width):
            printf(f" {i}")
        print("")
        print(f"_: 空({self.empties}), x:黒({self.blacks}), o:白({self.whites})")

    @property
    def whites(self):
        if not self._is_updated: self._update()
        return self._whites

    @property
    def blacks(self):
        if not self._is_updated: self._update()
        return self._blacks

    @property
    def empties(self):
        if not self._is_updated: self._update()
        return self._empties
