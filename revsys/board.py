import sys

from settings import TILE_MAX, WIDTH, HEIGHT, TILE_MAX

from .board_base import BoardBase
from .position import Position
from .state import State
from .tools import Const

class Board(BoardBase, Const):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT)
        self._board[HEIGHT//2-1][WIDTH//2-1] = State.BLACK
        self._board[HEIGHT//2-1][ WIDTH//2 ] = State.WHITE
        self._board[ HEIGHT//2 ][WIDTH//2-1] = State.WHITE
        self._board[ HEIGHT//2 ][ WIDTH//2 ] = State.BLACK
        """
        self._board = [[ 1,-1, 1,-1, 1,-1, 1,-1],
                       [ 1,-1, 1,-1, 1,-1, 1,-1],
                       [ 1,-1, 1,-1, 1,-1, 1,-1],
                       [ 1,-1, 1,-1, 1,-1, 1,-1],
                       [ 1,-1, 1,-1, 1,-1, 1,-1],
                       [ 1,-1, 1,-1, 1,-1, 1,-1],
                       [ 1,-1, 1,-1, 1,-1, 1,-1],
                       [ 1,-1, 1, 0, 0,-1, 1,-1]]
        """
    """
    game check code:
      0 : both players can put a stone somewhere legally
      1 : WHITE cannot put a stone but BLACK can
     -1 : BLACK cannot put a stone but WHITE can
     10 : DRAW
     11 : BLACK wins
      9 : WHITE wins
    """
    def game_check(self):
        if self.empties == 0:
            return self.result_check()
        else:
            black_puttable = white_puttable = False
            for n in range(TILE_MAX):
                if self.is_puttable(Position(n), State.BLACK): black_puttable = True
                if self.is_puttable(Position(n), State.WHITE): white_puttable = True
                if black_puttable and white_puttable: return 0
            if black_puttable: return 1
            if white_puttable: return -1
            return self.result_check()
            print("ここには来ない2")
            sys.exit()

    def result_check(self):
        if self.blacks > self.whites: return 11
        if self.whites > self.blacks: return 9
        if self.blacks == self.whites: return 10
        print("ここには来ない1")
        sys.exit()

    def is_puttable(self, p:Position, s:State):
        # range check
        if not p.is_in(): return False
        # empty check
        if not self.is_state(p, State.EMPTY): return False
        # reverse check
        tmpboard = self.clone()
        tmpboard.put_stone(p, s)
        return tmpboard._total_reversed_count > 0

    def put_stone(self, p: Position, s: State):
        self._total_reversed_count = 0
        self.set_state(p, s)
        if s == State.EMPTY:
            print("put stone!"); return False

        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                pp = p.clone()
                reverse_count = 0
                while pp.move_and_check(dx, dy):
                    # print(f"search [{dx}, {dy}], pp = ({p.x}, {p.y}), count = {reverse_count}")
                    if self.is_state(pp, State.EMPTY): break
                    if self.is_state(pp, -s):
                        reverse_count += 1; continue
                    if self.is_state(pp, s):
                        if reverse_count == 0: break
                        for _ in range(reverse_count):
                            pp.move(-dx, -dy)
                            self.set_state(pp, s)
                            self._total_reversed_count += 1
                        break

    def clone(self):
        b = Board()
        for i in range(HEIGHT):
            for j in range(WIDTH):
                b._board[i][j] = self._board[i][j]
        b._update()
        return b
