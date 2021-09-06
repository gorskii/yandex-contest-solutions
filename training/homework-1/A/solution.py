def get_resulting_temperature(t_current, t_target, mode):
    result = t_current

    if mode == 'fan':
        pass
    elif mode == 'auto':
        result = t_target
    elif mode == 'freeze':
        result = min(t_current, t_target)
    else:
        result = max(t_current, t_target)

    return result


if __name__ == '__main__':
    t_room, t_cond = tuple(map(int, input().strip().split()))
    mode = input().strip()

    print(get_resulting_temperature(t_room, t_cond, mode))
