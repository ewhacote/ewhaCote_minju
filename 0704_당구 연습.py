def distance_squared(number):
    return number**2

def find_minimum(*numbers):
    return min(numbers)

def calculate_minimum_distance(start_x, start_y, target_x, target_y, width, height):
    up = distance_squared(start_x - target_x) + distance_squared(2 * height - start_y - target_y)
    down = distance_squared(start_x - target_x) + distance_squared(start_y + target_y)
    left = distance_squared(start_x + target_x) + distance_squared(start_y - target_y)
    right = distance_squared(start_y - target_y) + distance_squared(2 * width - start_x - target_x)

    if start_x == target_x and target_y > start_y:
        return find_minimum(down, left, right)
    elif start_x == target_x and target_y < start_y:
        return find_minimum(up, left, right)
    elif start_y == target_y and target_x > start_x:
        return find_minimum(up, down, left)
    elif start_y == target_y and target_x < start_x:
        return find_minimum(up, down, right)
    else:
        return find_minimum(up, down, left, right)

def solution(m, n, start_x, start_y, balls):
    answer = [0]*len(balls)
    for i in range(len(balls)):
        target_x = balls[i][0]
        target_y = balls[i][1]
        answer[i] = calculate_minimum_distance(start_x, start_y, target_x, target_y, m, n)
    return answer
