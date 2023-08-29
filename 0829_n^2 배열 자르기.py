def solution(n, start, end):
    answer = []

    for i in range(start, end + 1):
        answer.append(max(i // n, i % n) + 1)

    return answer