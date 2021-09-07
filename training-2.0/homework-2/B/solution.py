def get_max_store_distance(buildings):
    """Return maximum distance from a house to the nearest store.

    buildings -- list of buildings, where each building is represented
    by a folowing number:

    0 - office building
    1 - house
    2 - store
    """
    max_distance = 0
    for i in range(0, len(buildings)):
        if buildings[i] == 1:
            left, right = i-1, i+1
            found_store = False
            while left >= 0 and right < len(buildings):
                if buildings[left] == 2 or buildings[right] == 2:
                    max_distance = max(max_distance, right - i)
                    found_store = True
                    break
                left -= 1
                right += 1
            while not found_store and left >= 0:
                if buildings[left] == 2:
                    max_distance = max(max_distance, i - left)
                    found_store = True
                    break
                left -= 1
            while not found_store and right < len(buildings):
                if buildings[right] == 2:
                    max_distance = max(max_distance, right - i)
                    found_store = True
                    break
                right += 1
    return max_distance


if __name__ == '__main__':
    buildings = list(map(int, input().split()))
    print(get_max_store_distance(buildings))
