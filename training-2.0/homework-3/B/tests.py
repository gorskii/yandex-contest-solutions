from solution import check_duplicates


cases = [
    (([1, 2, 3, 2, 3, 4], ), ['NO', 'NO', 'NO', 'YES', 'YES', 'NO']),
    (([1, 2, 1, 2], ), ['NO', 'NO', 'YES', 'YES']),
    (([1], ), ['NO']),
]

for case, expected in cases:
    try:
        result = check_duplicates(*case)
        assert result == expected
        print('OK')
    except AssertionError:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
