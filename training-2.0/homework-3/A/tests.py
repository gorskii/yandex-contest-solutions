from solution import count_matching_numbers


cases = [
    (({1, 3, 2}, {4, 3, 2}), 2),
    (({1, 2, 6, 4, 5, 7}, {10, 2, 3, 4, 8}), 2),
    (({1, 7, 3, 8, 10, 2, 5}, {6, 5, 2, 8, 4, 3, 7}), 5),
]

for case, expected in cases:
    try:
        result = count_matching_numbers(*case)
        assert result == expected
        print('OK')
    except AssertionError:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
