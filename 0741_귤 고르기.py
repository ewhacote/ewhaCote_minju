from collections import Counter

def solution(k, t):
    answer = 0
    c = Counter(t).most_common()

    for i in range(len(c)):
        if c[i][1] >= k:
            answer += 1
            break
        else:
            k -= c[i][1]
            answer += 1

    return answer
