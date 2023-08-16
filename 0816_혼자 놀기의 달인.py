//다시 풀어보기

def solution(cards):
    answer = []
    
    for i in range(len(cards)):
        tmp = []
        while cards[i] not in tmp:
            tmp.append(cards[i])
            i = cards[i]-1
    
        if sorted(tmp) in answer:
            answer.append([])
        else:
            answer.append(sorted(tmp))
        
    answer.sort(key=len)
        
    return len(answer[-1]) * len(answer[-2])