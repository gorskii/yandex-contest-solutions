from collections import defaultdict


def get_unique_numbers(nums):
    """Return list of unique numbers in nums."""
    nums_frequency = defaultdict(int)
    for num in nums:
        nums_frequency[num] += 1
    return [num for num in nums if nums_frequency[num] == 1]


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    print(' '.join(map(str, get_unique_numbers(numbers))))
