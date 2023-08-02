def collatz_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        n = n / 2 if n % 2 == 0 else n * 3 + 1
    sequence.append(n)
    return sequence

def solution(n, ranges):
    answer = []
    sequence = collatz_sequence(n)
    for range_values in ranges:
        start_index, end_index = range_values
        sliced_sequence = sequence[start_index:len(sequence)+end_index]
        if start_index >= end_index+len(sequence):
            answer.append(-1)
            continue
        sum_total = 0
        for i in range(len(sliced_sequence)-1):
            sum_total += ((sliced_sequence[i] + sliced_sequence[i+1])/2)
        answer.append(sum_total)
    return answer
