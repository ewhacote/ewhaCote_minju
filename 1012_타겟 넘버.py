from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)])

    count = 0
    
    while queue:
        index, cur_sum = queue.popleft()

        if index == len(numbers):
            if cur_sum == target:
                count += 1
        else:
            queue.append((index + 1, cur_sum + numbers[index]))
            queue.append((index + 1, cur_sum - numbers[index]))
    
    return count

