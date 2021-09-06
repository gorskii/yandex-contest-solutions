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

    if (x >= 0 and y >= 0) and ((x - B.x) * (C.y - B.y) - (y - B.y) * (C.x - B.x) <= 0):
        return 0

    status = -1
    minimum = 10000000
    nearest_vertex = -1
    for i, vertex in enumerate((A, B, C)):
        dist = Point(x, y) - vertex
        if dist < minimum:
            minimum = dist
            nearest_vertex = i + 1
    status = nearest_vertex

    return status


if __name__ == '__main__':
    side = int(input())
    x, y = map(int, input().split())

    print(get_point_status(side, x, y))
