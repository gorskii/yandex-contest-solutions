def get_shortest_route(total, start, finish):
    forward = abs(finish - start) - 1
    backwards = total - forward - 2
    return min(forward, backwards)


if __name__ == '__main__':
    total, start, finish = map(int, input().split())

    print(get_shortest_route(total, start, finish))
