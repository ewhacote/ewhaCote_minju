def solution(nums):
    answer = []
    
    def calc(x):
        l = (~x) & (x + 1)
        return (x | l) & ~(l >> 1)
        
    for n in nums:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            answer.append(calc(n))
    
    return answer
