from solution import min_substitutions_to_make_palindrome


cases = [
    (('a',), 0),
    (('ab',), 1),
    (('cognitive',), 4),
]

for case, expected in cases:
    try:
        result = min_substitutions_to_make_palindrome(*case)
        assert result == expected
        print('OK')
    except AssertionError:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
