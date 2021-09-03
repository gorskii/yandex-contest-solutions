from solution import check_date_is_unambiguous


cases = [
    ((1, 2, 2003), 0),
    ((2, 29, 2008), 1),
    ((13, 1, 2018), 1),
    ((7, 15, 2018), 1),
    ((12, 7, 2018), 0),
    ((12, 12, 2018), 1),
    ((7, 7, 2018), 1),
]

for case, expected in cases:
    try:
        result = check_date_is_unambiguous(*case)
        assert result == expected
        print('OK')
    except AssertionError as e:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
