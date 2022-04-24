from .system import System
from .position import Position

def cui_game():
    print("ゲームを開始します")
    s = System()
    while s.can_next():
        print("=====================================")
        print("xとyはそれぞれ0から7の範囲内で入力してください(-1で終了)")
        s.prints()
        while True:
            x = int(input("x: "))
            if x == -1: return
            y = int(input("y: "))
            if -1 < x < 8 and -1 < y < 8: break
            print("xとyはそれぞれ0から7の範囲内で入力してください(-1で終了)")
        s.put_stone(Position(x, y))
    print("ゲームを終了しました")
