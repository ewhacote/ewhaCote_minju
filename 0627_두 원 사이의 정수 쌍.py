def solution(r1, r2):
    answer = 0
    for i in range(1, r2):
        y2 = int((r2**2 - i**2)**0.5)
        if i >= r1:
            answer += 4 * (y2 + 1)
        else:
            y1 = int((r1**2 - i**2)**0.5)
            if y1**2 + i**2 == r1**2:
                answer += 4 * (y2 - y1 + 1)
            else:
                answer += 4 * (y2 - y1)
    answer += 4
    return answer