from solution import get_max_store_distance


cases = [
    (([2, 0, 1, 1, 0, 1, 0, 2, 1, 2],), 3),
]

for case, expected in cases:
    try:
        result = get_max_store_distance(*case)
        assert result == expected
        print('OK')
    except AssertionError:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
