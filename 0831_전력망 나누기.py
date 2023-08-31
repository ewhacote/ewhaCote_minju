#풀이 부족. 다시 풀어보기

from collections import deque

def BFS(start, graph, visited, check_link):
        q = deque([start])
        visited[start] = True
        cnt = 1
        while q:
            s = q.popleft()
            for adj_v in graph[s]:
                if visited[adj_v] == False and check_link[start][adj_v]: 
                    q.append(adj_v)
                    visited[adj_v] = True
                    cnt += 1
        return cnt

def solution(n, wires):
    answer = n
    
    # 끊은 간선인지 아닌지 체크하기 위한 리스트 
    check_link = [[True]*(n+1) for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]    # 송전탑 그래프 

    # 그래프 채우기 
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    for a,b in wires:                               
        visited = [False]*(n+1)                     
        check_link[a][b] = False                    
        cnt_a = BFS(a, graph, visited, check_link)  
        cnt_b = BFS(b, graph, visited, check_link)  
        check_link[a][b] = True                     
        
        answer = min(answer, abs(cnt_a - cnt_b))
    
    
    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))
