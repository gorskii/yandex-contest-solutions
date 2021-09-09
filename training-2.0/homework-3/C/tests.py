from solution import get_unique_numbers


cases = [
    (([1, 2, 2, 3, 3, 3], ), [1]),
    (([4, 3, 5, 2, 5, 1, 3, 5], ), [4, 2, 1]),
]

for case, expected in cases:
    try:
        result = get_unique_numbers(*case)
        assert result == expected
        print('OK')
    except AssertionError:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
