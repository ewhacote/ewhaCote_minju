def solution(target, quantities, sequence):
    answer = 0
    total_quantity = sum(quantities)

    for i in range(len(sequence) - total_quantity + 1):
        target_quantities = dict(zip(target, quantities))
        for item in sequence[i:i + total_quantity]:
            if item not in target_quantities:
                break
            target_quantities[item] -= 1
            if target_quantities[item] < 0:
                break
        else:  # No break occurred
            if all(val == 0 for val in target_quantities.values()):
                answer += 1

    return answer
