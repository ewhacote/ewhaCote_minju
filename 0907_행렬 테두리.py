def solution(rows, columns, queries):
    answer = []
    matrix = []
    
    # 행렬 초기화
    for r in range(rows):
        matrix.append([val for val in range(r * columns + 1, (r + 1) * columns + 1)])
    
    for query in queries:
        query = [x - 1 for x in query]  # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
        tmp = matrix[query[0]][query[1]]  # 왼쪽 위 값 저장
        smallest = tmp
        
        # 왼쪽
        for i in range(query[0] + 1, query[2] + 1):
            matrix[i - 1][query[1]] = matrix[i][query[1]]
            smallest = min(smallest, matrix[i][query[1]])
        
        # 아래
        for i in range(query[1] + 1, query[3] + 1):
            matrix[query[2]][i - 1] = matrix[query[2]][i]
            smallest = min(smallest, matrix[query[2]][i])
        
        # 오른쪽
        for i in range(query[2] - 1, query[0] - 1, -1):
            matrix[i + 1][query[3]] = matrix[i][query[3]]
            smallest = min(smallest, matrix[i][query[3]])
        
        # 위
        for i in range(query[3] - 1, query[1] - 1, -1):
            matrix[query[0]][i + 1] = matrix[query[0]][i]
            smallest = min(smallest, matrix[query[0]][i])
        
        matrix[query[0]][query[1] + 1] = tmp
        
        answer.append(smallest)
    
    return answer
