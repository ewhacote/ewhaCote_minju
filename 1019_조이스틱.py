def solution(name):
    move = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    idx = 0
    answer = 0
    
    while True:
        answer += move[idx]
        move[idx] = 0
        if sum(move) == 0:
            break
        
        left, right = 1, 1
        while move[idx - left] == 0:
            left += 1
        while move[idx + right] == 0:
            right += 1
        
        if left < right:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right
    
    return answer
