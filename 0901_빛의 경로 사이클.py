def solution(grid):
    answer = []
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    vis = set()

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for d in range(4):
                if (x, y, d) in vis:
                    continue
                
                cnt = 0
                cx, cy, cd = x, y, d

                while (cx, cy, cd) not in vis:
                    vis.add((cx, cy, cd))
                    cnt += 1

                    dx, dy = dir[cd]
                    nx = (cx + dx) % len(grid)
                    ny = (cy + dy) % len(grid[0])

                    if grid[nx][ny] == 'L':
                        nd = (cd - 1) % 4
                    elif grid[nx][ny] == 'R':
                        nd = (cd + 1) % 4
                    else:
                        nd = cd

                    cx, cy, cd = nx, ny, nd

                answer.append(cnt)

    return sorted(answer)

