def get_school_coordinates(coordinates):
    current_sum = 0
    for num in coordinates:
        current_sum += abs(coordinates[0] - num)

    minimal_sum = current_sum
    school_coordinates = coordinates[0]
    left, right = 0, len(coordinates)
    while left <= right:
        mid = (right + left) // 2
        current_sum = 0
        for num in coordinates:
            current_sum += abs(coordinates[mid] - num)
        if current_sum < minimal_sum:
            minimal_sum = current_sum
            school_coordinates = coordinates[mid]
            left = mid + 1
        else:
            right = mid - 1

    return school_coordinates


if __name__ == '__main__':
    N = int(input())
    coordinates = [int(x) for x in input().split()]

    print(get_school_coordinates(coordinates))
