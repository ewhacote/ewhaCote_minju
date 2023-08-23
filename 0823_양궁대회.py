from itertools import combinations_with_replacement

def solution(n, info):
    answer = [0] * 11
    max_diff = 0

    for res in combinations_with_replacement(range(11), n):
        now = [0] * 11
        for r in res:
            now[10 - r] += 1

        lion, peach = 0, 0
        for i, (l, p) in enumerate(zip(now, info)):
            if l > p:
                lion += (10 - i)
            elif p > 0:
                peach += (10 - i)

        if lion > peach and (lion - peach) > max_diff:
            max_diff = lion - peach
            answer = now

    return answer if max_diff > 0 else [-1]

