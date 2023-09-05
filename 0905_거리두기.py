def check_distance(room):
    for r in range(5):
        for c in range(5):
            if room[r][c] == 'P':
                # 상하좌우 체크
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 5 and 0 <= nc < 5 and room[nr][nc] == 'P':
                        return 0
                # 대각선 체크
                for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 5 and 0 <= nc < 5 and room[nr][nc] == 'P':
                        if room[r][nc] != 'X' or room[nr][c] != 'X':
                            return 0
                # 거리 2 체크
                for dr, dc in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 5 and 0 <= nc < 5 and room[nr][nc] == 'P':
                        if room[(r + nr) // 2][(c + nc) // 2] != 'X':
                            return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(check_distance(place))
    return answer
