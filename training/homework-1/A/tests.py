from solution import get_resulting_temperature


cases = [
    ((10, 20, 'heat'), 20),
    ((10, 20, 'freeze'), 10),
    ((20, 10, 'fan'), 20),
    ((20, 10, 'auto'), 10),
    ((10, 20, 'auto'), 20),
]

for case, expected in cases:
    try:
        result = get_resulting_temperature(*case)
        assert result == expected
    except AssertionError as e:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
