def solution(priorities, location):
    from collections import deque

    q = deque([(v, i) for i, v in enumerate(priorities)])

    answer = 0
    while q:
        cur = q.popleft()
        if any(cur[0] < x[0] for x in q):
            q.append(cur)
        else:
            answer += 1
            if cur[1] == location:
                return answer