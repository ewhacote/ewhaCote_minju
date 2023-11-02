def solution(clothes):
    type_count = {}
    
    for item in clothes:
        type = item[1]
        type_count[type] = type_count.get(type, 0) + 1

    answer = 1
    for count in type_count.values():
        answer *= (count + 1)

    return answer - 1
