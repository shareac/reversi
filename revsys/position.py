from settings import WIDTH, HEIGHT

class Position:
    def __init__(self, n):
        self._x = n % WIDTH
        self._y = n // WIDTH

    def set(x, y):
        self._x, self._y = x, y

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def move_and_check(self, dx, dy, xmin=0, xmax=WIDTH, ymin=0, ymax=HEIGHT):
        self._x += dx
        self._y += dy
        return self.is_in()

    def is_in(self, xmin=0, xmax=WIDTH, ymin=0, ymax=HEIGHT):
        return (xmin <= self._x < xmax and ymin <= self._y < ymax)

    def clone(self):
        return Position(self._x + self._y * WIDTH)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
