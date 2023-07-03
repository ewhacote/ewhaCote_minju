from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def BFS(start):
    q = deque([start])
    
    while(q):
        y, x, dist =  q.popleft()

        if board[y][x] == 'G':
            return dist

        for i in range(4):
            ny = y
            nx = x
            while(True):
                # 다음 이동이 보드 내부일 경우
                if 0 <= ny + dy[i] <h and 0 <= nx + dx[i] < w: 
                    # 다음 위치가 블록된 경우
                    if board[ny + dy[i]][nx + dx[i]] == 'D': 
                        # 현재 위치를 아직 방문하지 않았다면
                        if visited[ny][nx] == False: 
                            q.append((ny, nx, dist + 1))
                            visited[ny][nx] = True
                            break
                        else:
                            break
                    else: # 다음 위치로 이동 가능한 경우
                        ny += dy[i]
                        nx += dx[i]   
                else: # 다음 이동이 보드 밖일 경우
                    # 현재 위치를 아직 방문하지 않았다면
                    if visited[ny][nx] == False: 
                        q.append((ny, nx, dist + 1))
                        visited[ny][nx] = True
                        break
                    else: 
                        break
    return -1   

def solution(b):
    global board
    global h
    global w
    global visited
    
    board = []
    h = len(b)
    w = len(b[0])
    visited = [[False for i in range(w)] for j in range(h)]
    for i in b:
        board.append(list(i))
        
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'R':
                visited[i][j] = True
                min_dist = BFS((i,j,0))

    return min_dist
