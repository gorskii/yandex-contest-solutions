def get_nums():
    """Generator that yields integers from stdin until 0 is given.

    Used to make get_max_count() testable.
    """
    num = -1
    while num != 0:
        num = int(input())
        yield num


def get_max_count(nums):
    max_count = 0
    max_num = -1
    for num in nums:
        if num > max_num:
            max_num = num
            max_count = 1
        elif num == max_num:
            max_count += 1
    return max_count

if __name__ == '__main__':
    print(get_max_count(get_nums()))
