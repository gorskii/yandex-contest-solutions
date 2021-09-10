def get_max_store_distance(buildings):
    """Return maximum distance from a house to the nearest store.

    buildings -- list of buildings, where each building is represented
    by a folowing number:

    0 - office building
    1 - house
    2 - store
    """
    dist_to_left_store = [0] * len(buildings)
    # given 10 buildings in problem statement, we make 'infinite' distance for the leftmost house
    store_position = -100
    for i in range(len(buildings)):
        if buildings[i] == 2:
            store_position = i
        if buildings[i] == 1:
            dist_to_left_store[i] = i - store_position
    # 'infinite' distance for the rightmost house, aswell
    store_position = 100
    max_distance = 0
    for i in range(len(buildings)-1, -1, -1):
        if buildings[i] == 2:
            store_position = i
        if buildings[i] == 1:
            min_distance = min(dist_to_left_store[i], store_position - i)
            max_distance = max(max_distance, min_distance)
    return max_distance


if __name__ == '__main__':
    buildings = list(map(int, input().split()))
    print(get_max_store_distance(buildings))
