def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for i, c in enumerate(citations):
        if i + 1 <= c:
            answer = i + 1
    return answer
