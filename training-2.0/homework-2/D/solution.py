def get_remaining_legs(bench_length, legs):
    """Return remaining legs for bench to stand still.

    Legs are enumerated from zero. Each leg is 1 unit wide, so
    if leg[i] == 1, it is 1 unit apart from the left side of the bench.
    """
    mid = bench_length // 2
    for i in range(len(legs)):
        # search for the first leg after the bench center or the middle leg
        if legs[i] >= mid:
            # if leg is in the middle of bench, it's the only leg needed
            if bench_length % 2 == 1 and legs[i] == mid:
                return (legs[i], )
            return (legs[i-1], legs[i])


if __name__ == '__main__':
    bench_length, legs_count = map(int, input().split())
    legs = list(map(int, input().split()))
    print(*get_remaining_legs(bench_length, legs))
