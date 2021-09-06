def are_equal(first, second):
    # skip 7 and 8, so number format is 4951234567
    for i in range(1, len(first)):
        if first[i] != second[i]:
            return False
    return True


def get_normalized_number(number, delimiters_set):
    result = ''.join(c for c in number if c not in delimiters_set)
    if len(result) == 7:
        result = '8495' + result
    return result


def get_check_results(number_to_check, numbers_list):
    match_results = []
    delimiters = set('+-()')

    target = get_normalized_number(number_to_check, delimiters)
    for number in numbers_list:
        candidate = get_normalized_number(number, delimiters)
        match_results.append('YES' if are_equal(target, candidate) else 'NO')

    return match_results


if __name__ == '__main__':
    number_to_check = input().strip()
    numbers_list = [input().strip() for _ in range(3)]

    for result in get_check_results(number_to_check, numbers_list):
        print(result)
