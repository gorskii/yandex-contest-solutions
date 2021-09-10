def get_school_coordinates(coordinates):
    return coordinates[len(coordinates) // 2]


if __name__ == '__main__':
    N = int(input())
    coordinates = list(map(int, input().split()))

    print(get_school_coordinates(coordinates))
