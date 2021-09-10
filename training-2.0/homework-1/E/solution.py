def get_point_status(d, x, y):
    """
    Return status of (x, y) point in relation to d-sided isosceles
    right triangle ABC, where AB == AC.

    0 - inside the triangle
    1 - A is nearest vertex
    2 - B is nearest vertex
    3 - C is nearest vertex
    """
    if x >= 0 and y >= 0 and x + y <= d:
        return 0
    # we can eliminate square root in (x**2 + y**2)**0.5, since x**2 + y**2 >= 0
    distances = [(x**2 + y**2, 1), ((x - d)**2 + y**2, 2), (x**2 + (y - d)**2, 3)]
    return min(distances)[1]


if __name__ == '__main__':
    side = int(input())
    x, y = map(int, input().split())

    print(get_point_status(side, x, y))
