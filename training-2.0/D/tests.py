from solution import get_school_coordinates


cases = [
    (([1, 2, 3, 4]), (2, 3)),
    (([-1, 0, 1]), (0,)),
    # -1 0 1 2 3 4 5 6
    # -4 1 3 18
    # -95 0 64 124 359
    # -1 5 300
    (([-1, 5, 6]), (5,)),
    (([-95, 0, 64, 124, 359]), (64,)),
]

for case, expected in cases:
    try:
        result = get_school_coordinates(case)
        assert result in expected
        print('OK')
    except AssertionError:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
