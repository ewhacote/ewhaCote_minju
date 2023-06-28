def solution(sequence, k):
    answer = [0, len(sequence)-1] 
    left, right = 0, 0
    sum = sequence[0]

    while left <= right and right < len(sequence):
        if sum < k:
            right += 1
            if right < len(sequence):
                sum += sequence[right]
        elif sum == k:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            sum -= sequence[left]
            left += 1
        else: 
            sum -= sequence[left]
            left += 1
    return answer