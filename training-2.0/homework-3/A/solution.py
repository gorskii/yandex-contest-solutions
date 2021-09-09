def count_matching_numbers(a, b):
    """Return number of elements contained both in a and b."""
    return sum(1 for num in a if num in b)


if __name__ == '__main__':
    first_set = set(map(int, input().split()))
    second_set = set(map(int, input().split()))
    print(count_matching_numbers(first_set, second_set))
