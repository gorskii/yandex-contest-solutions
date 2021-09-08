def get_minimal_time_to_search(diplomas):
    """Return minimal required time to search folders for a specific diploma."""
    # the last folder is the one with a target in the worst case
    return sum(sorted(diplomas)[:-1])


if __name__ == '__main__':
    folders_count = int(input())
    diplomas = list(map(int, input().split()))
    print(get_minimal_time_to_search(diplomas))
