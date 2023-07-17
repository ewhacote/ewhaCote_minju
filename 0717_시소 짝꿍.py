def solution(weights):
    weight_count = {}
    for weight in weights:
        weight_count[weight] = weight_count.get(weight, 0) + 1

    pair_count = 0

    for weight in weights:
        if weight % 2 == 0: 
            pair_count += weight_count.get(weight * 3 // 2, 0)

        if weight % 3 == 0: 
            pair_count += weight_count.get(weight * 4 // 3, 0)

        pair_count += weight_count.get(weight * 2, 0)

    for weight in weights:
        weight_count[weight] -= 1
        pair_count += weight_count[weight]
    
    return pair_count
