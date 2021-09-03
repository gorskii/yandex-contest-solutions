def check_date_is_unambiguous(x, y, z):
    return 1 if (x > 12 or y > 12 or x == y) else 0


if __name__ == '__main__':
    x, y, z = map(int, input().split())

    print(check_date_is_unambiguous(x, y, z))
