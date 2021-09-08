from solution import get_remaining_legs


cases = [
    ((5, [0, 2]), (2, )),
    ((13, [1, 4, 8, 11]), (4, 8)),
    ((14, [1, 6, 8, 11, 13]), (6, 8)),
    ((4, [0, 2, 3]), (0, 2)),
    ((5, [2]), (2, )),
]

for case, expected in cases:
    try:
        result = get_remaining_legs(*case)
        assert result == expected
        print('OK')
    except AssertionError:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
