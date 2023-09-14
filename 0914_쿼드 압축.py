def compress(arr, x, y, n, answer):
    if n == 1:
        answer[arr[x][y]] += 1
        return
    
    first_value = arr[x][y]
    same_value = all(arr[i][j] == first_value for i in range(x, x + n) for j in range(y, y + n))
    
    if same_value:
        answer[first_value] += 1
    else:
        half_n = n // 2
        compress(arr, x, y, half_n, answer)
        compress(arr, x + half_n, y, half_n, answer)
        compress(arr, x, y + half_n, half_n, answer)
        compress(arr, x + half_n, y + half_n, half_n, answer)

def solution(arr):
    answer = [0, 0]
    compress(arr, 0, 0, len(arr), answer)
    return answer
 