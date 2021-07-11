from solution import solve


cases = [
    ((1, 0, 0), '0'),
    ((1, 2, 3), '7'),
    ((1, 2, -3), 'NO SOLUTION'),
    ((0, 0, 0), 'MANY SOLUTIONS'),
    ((0, 1, 1), 'MANY SOLUTIONS'),
    ((1, 0, 1), '1'),
    ((-1, 0, 1), '-1'),
]

for case, expected in cases:
    try:
        result = solve(*case)
        assert result == expected
    except AssertionError as e:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
