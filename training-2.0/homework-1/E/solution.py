class Point:
    """A two-dimensional point"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, point):
        return ((self.x-point.x)**2 + (self.y-point.y)**2) ** 0.5


def get_point_status(d, x, y):
    """
    Return status of (x, y) point in relation to d-sided isosceles
    right triangle ABC, where AB == AC.

    0 - inside the triangle
    1 - A is nearest vertex
    2 - B is nearest vertex
    3 - C is nearest vertex
    """
    A = Point(0, 0)
    B = Point(d, 0)
    C = Point(0, d)

    if x >= 0 and y >= 0 and x + y <= d:
        return 0

    point = Point(x, y)
    distances = [(point - A, 1), (point - B, 2), (point - C, 3)]
    return min(distances)[1]


if __name__ == '__main__':
    side = int(input())
    x, y = map(int, input().split())

    print(get_point_status(side, x, y))
