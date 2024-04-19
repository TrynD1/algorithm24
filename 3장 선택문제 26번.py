def dfs_spanning_tree(graph, start):
    n = len(graph)
    visited = [False] * n
    edges = []  # 신장 트리를 구성하는 간선들을 저장
    stack = [start]

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            for neighbor in range(n):
                if graph[vertex][neighbor] != 0 and not visited[neighbor]:
                    edges.append((vertex, neighbor))  # 신장 트리에 간선 추가
                    stack.append(neighbor)

    return edges

# 예제 그래프 (연결 행렬)
graph = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0]
]

# 시작 정점을 0으로 하여 신장 트리 구하기
spanning_tree_edges = dfs_spanning_tree(graph, 0)
print("Edges in the spanning tree:", spanning_tree_edges)
