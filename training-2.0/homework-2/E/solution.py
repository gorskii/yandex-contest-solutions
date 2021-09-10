def get_minimal_time_to_search(diplomas):
    """Return minimal required time to search folders for a specific diploma."""
    # largest folder is the one with a target in the worst case
    return sum(diplomas) - max(diplomas)


if __name__ == '__main__':
    folders_count = int(input())
    diplomas = list(map(int, input().split()))
    print(get_minimal_time_to_search(diplomas))
