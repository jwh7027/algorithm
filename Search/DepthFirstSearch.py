#DFS 그래프
#인접리스트
graph = {
    'A' : ['B', 'D', 'E'],
    'B' : ['A', 'C', 'D'],
    'C' : ['B'],
    'D' : ['A' , 'B'],
    'E' : ['A']
}

visited = [] # 각 노드가 방문된 정보를 리스트 자료형으로 표현
def dfs(cur_v):
    # 현재 노드를 visited 삽입
    visited.append(cur_v)
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for v in graph[cur_v]:
        if v not in visited:
            dfs(v)
    return visited
dfs('A')
#출력 ['A', 'B', 'C', 'D', 'E']