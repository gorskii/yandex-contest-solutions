from solution import get_point_status


cases = [
    ((5, 1, 1), 0),
    ((3, -1, -1), 1),
    ((4, 4, 4), 2),
    ((4, 2, 2), 0),
]

for case, expected in cases:
    try:
        result = get_point_status(*case)
        assert result == expected
        print('OK')
    except AssertionError:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
