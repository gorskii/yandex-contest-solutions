from solution import get_check_results


cases = [
    (
        (
            '8(495)430-23-97',
            [
                '+7-4-9-5-43-023-97',
                '4-3-0-2-3-9-7',
                '8-495-430',
            ],
        ),
        [
            'YES',
            'YES',
            'NO',
        ],
    ),
    (
        (
            '86406361642',
            [
                '83341994118',
                '86406361642',
                '83341994118',
            ],
        ),
        [
            'NO',
            'YES',
            'NO',
        ],
    ),
    (
        (
            '+78047952807',
            [
                '+78047952807',
                '+76147514928',
                '88047952807',
            ],
        ),
        [
            'YES',
            'NO',
            'YES',
        ],
    ),
    (
        (
            '8952807',
            [
                '+78048952807',
                '7952807',
                '84958952807',
            ],
        ),
        [
            'NO',
            'NO',
            'YES',
        ],
    ),
]

for case, expected in cases:
    try:
        result = get_check_results(*case)
        assert result == expected
    except AssertionError as e:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
