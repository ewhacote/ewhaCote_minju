def solution(w):
    answer = 0
    for i, c in enumerate(w):
        answer += (5 ** (5 - i) - 1) // 4 * "AEIOU".index(c) + 1
    return answer
