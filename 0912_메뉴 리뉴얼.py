from collections import Counter
from itertools import combinations

def solution(orders, course):
    ans = []

    for c in course:
        combs = [comb for order in orders for comb in combinations(sorted(order), c)]
        count = Counter(combs)
        if count:
            max_freq = count.most_common(1)[0][1]
            ans += [k for k, v in count.items() if v == max_freq and v > 1]

    return [''.join(t) for t in sorted(ans)]
