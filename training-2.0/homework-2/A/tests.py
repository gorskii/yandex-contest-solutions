from solution import get_max_count


cases = [
    (([1, 7, 9, 0],), 1),
    (([1, 3, 3, 1, 0],), 2),
]

for case, expected in cases:
    try:
        result = get_max_count(*case)
        assert result == expected
        print('OK')
    except AssertionError:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
