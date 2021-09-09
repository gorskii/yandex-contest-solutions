def check_duplicates(nums):
    """Check if number occured once in the list or not.

    Return list of YES and NO.
    """
    answer = []
    nums_set = set()
    for num in nums:
        if num in nums_set:
            answer.append('YES')
        else:
            nums_set.add(num)
            answer.append('NO')
    return answer


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    for answer in check_duplicates(numbers):
        print(answer)
