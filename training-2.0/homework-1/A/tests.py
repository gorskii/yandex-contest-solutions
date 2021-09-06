from solution import get_result_code


cases = [
    ((0, 0, 0), 0),
    ((-1, 0, 1), 3),
    ((42, 1, 6), 6),
    ((44, 7, 4), 1),
    ((1, 4, 0), 3),
    ((-3, 2, 4), 2),
]

for case, expected in cases:
    try:
        result = get_result_code(*case)
        assert result == expected
        print('OK')
    except AssertionError:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
