def solution(dirs):
    visited = set()
    x, y = 0, 0

    for dir in dirs:
        nx, ny = x, y
        if dir == 'U' and y + 1 <= 5:
            ny += 1
        elif dir == 'D' and y - 1 >= -5:
            ny -= 1
        elif dir == 'R' and x + 1 <= 5:
            nx += 1
        elif dir == 'L' and x - 1 >= -5:
            nx -= 1
        
        if (x, y, nx, ny) not in visited:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
        x, y = nx, ny

    return len(visited) // 2
