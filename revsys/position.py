class Position:
    def __init__(self, x, y):
        self._x, self._y = x, y

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def move_and_check(self, dx, dy, xmin, xmax, ymin, ymax):
        self._x += dx
        self._y += dy
        return self.is_in(xmin, xmax, ymin, ymax)

    def is_in(self, xmin, xmax, ymin, ymax):
        return (xmin <= self._x < xmax and ymin <= self._y < ymax)

    def clone(self):
        return Position(self._x, self._y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
