from solution import get_minimal_time_to_search


cases = [
    (([2, 1], ), 1),
]

for case, expected in cases:
    try:
        result = get_minimal_time_to_search(*case)
        assert result == expected
        print('OK')
    except AssertionError:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
