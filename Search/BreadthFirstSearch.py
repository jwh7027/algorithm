#BFS 그래프
#인접리스트
graph = {
    'A' : ['B', 'D', 'E'],
    'B' : ['A', 'C', 'D'],
    'C' : ['B'],
    'D' : ['A' , 'B'],
    'E' : ['A']
}
from collections import deque
# 큐(Queue) 구현을 위해 deque 라이브러리 사용
def bfs(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        cur_v = queue.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited
bfs(graph, 'A')
#출력 ['A', 'B', 'D', 'E', 'C']