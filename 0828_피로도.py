from itertools import permutations

def solution(k, d):
    answer = 0
    n = len(d)
    for p in permutations(d, n):
        tk = k
        cnt = 0
        for x in p:
            if tk >= x[0]:
                tk -= x[1]
                cnt += 1
        answer = max(answer, cnt)
    return answer
