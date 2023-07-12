from collections import deque

def bfs(island, sy, sx, w, h):
    cnt = int(island[sy][sx])
    q = deque([(sy, sx)])
    island[sy][sx] = 'X'

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        a, b = q.popleft()

        for i in range(4):
            y = a + dy[i]
            x = b + dx[i]

            if 0 <= y < h and 0 <= x < w and island[y][x].isdigit():
                cnt += int(island[y][x])
                island[y][x] = 'X'
                q.append((y, x))

    return island, cnt


def solution(maps):
    answer = []
    w, h = len(maps[0]), len(maps)

    for i in range(h):
        maps[i] = list(maps[i])

    for i in range(h):
        for j in range(w):
            if maps[i][j].isdigit():
                maps, day = bfs(maps, i, j, w, h)
                answer.append(day)

    if answer:
        answer.sort()
        return answer
    else:
        return [-1]
