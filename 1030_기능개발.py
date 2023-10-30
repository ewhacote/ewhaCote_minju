def solution(progresses, speeds):
    days = [(100 - p + s - 1) // s for p, s in zip(progresses, speeds)]
    stack = []
    answer = []

    for day in days:
        if stack and stack[-1] < day:
            answer.append(len(stack))
            stack = []
        stack.append(day)

    if stack:
        answer.append(len(stack))
        
    return answer
