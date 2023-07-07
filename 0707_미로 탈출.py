from collections import deque

def solution(maps):
    answer = 0
    open = False

    visited = [[0] *len(maps[0]) for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
                visited[i][j] = 1
                break

    q = deque()
    q.append((start[0], start[1]))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 이동 가능한 4방위 탐색을 설정해줍니다.

    while q:
        x, y = q.popleft()
        if maps[x][y] == 'L' and not open:
            answer += visited[x][y]
            open = True
            visited = [[0] *len(maps[0]) for _ in range(len(maps))]
            visited[x][y] = 1
            q = deque()
            q.append((x, y))
            continue


        if maps[x][y] == 'E' and open:
            answer += visited[x][y]
            return answer - 2

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx in range(len(maps)) and ny in range(len(maps[0])):
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    answer = -1
    return answer
