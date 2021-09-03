def get_shortest_route(total, start, finish):
    if start > finish:
        start, finish = finish, start
    return min(finish - start - 1, start + (total - finish) - 1)


if __name__ == '__main__':
    total, start, finish = map(int, input().split())

    print(get_shortest_route(total, start, finish))

