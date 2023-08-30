from itertools import combinations

def find_intersection(l1, l2):
    a, b, e = l1
    c, d, f = l2
    if a * d == b * c:
        return
    x = (b * f - e * d) / (a * d - b * c)
    y = (e * c - a * f) / (a * d - b * c)
    if x == int(x) and y == int(y):
        return int(x), int(y)

def solution(line):
    pts = set()
    x_pts, y_pts = set(), set()
    for a, b in combinations(line, 2):
        pt = find_intersection(a, b)
        if pt:
            pts.add(pt)
            x_pts.add(pt[0])
            y_pts.add(pt[1])

    x_min, x_max = min(x_pts), max(x_pts)
    y_min, y_max = min(y_pts), max(y_pts)

    ans = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]
    for x, y in pts:
        ans[y_max - y][x - x_min] = '*'
    return [''.join(row) for row in ans]
