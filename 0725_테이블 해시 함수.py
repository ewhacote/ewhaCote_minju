def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))

    for row_idx in range(row_begin, row_end + 1):
        total = 0
        for value in data[row_idx - 1]:
            total += (value % row_idx)
        answer ^= total

    return answer
