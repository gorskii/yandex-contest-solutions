from solution import get_shortest_route


cases = [
    ((100, 5, 6), 0),
    ((10, 1, 9), 1),
    ((2, 1, 2), 0),
    ((4, 1, 3), 1),
    ((100, 99, 60), 38),
]

for case, expected in cases:
    try:
        result = get_shortest_route(*case)
        assert result == expected
        print('OK')
    except AssertionError as e:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
