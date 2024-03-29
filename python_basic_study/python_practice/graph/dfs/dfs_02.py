class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

    def print_graph(self):
        for row in self.graph:
            print(row)


num_of_vertex = 6
g1 = Graph(num_of_vertex + 1)
g1.graph[1][2] = 1
g1.graph[2][1] = 1
g1.graph[3][1] = 1
g1.graph[1][3] = 1
g1.graph[2][4] = 1
g1.graph[4][2] = 1
g1.graph[3][4] = 1
g1.graph[4][3] = 1
g1.graph[5][4] = 1
g1.graph[4][5] = 1
g1.graph[4][6] = 1
g1.graph[6][4] = 1
g1.graph[5][6] = 1
g1.graph[6][5] = 1
g1.print_graph()

#
stack = []
visited = []

# Initial Vertex
current = 1
stack.append(current)
visited.append(current)

# DFS start
while stack:
    next_ = None

    # current 와 연결된 정점을 전체 정점을 순회하며 찾는다
    for vertex in range(1, g1.SIZE):
        if g1.graph[current][vertex] == 1:
            # 연결된 정점을 찾았다면 방문 목록에 있는지 확인하고 없을 경우에만 next_ 에 방문 정점을 저장
            if vertex not in visited:
                next_ = vertex
                break

    # 만약 새 정점이 있었다면 스택과 방문 목록에 저장한다
    if next_ is not None:
        current = next_
        stack.append(current)
        visited.append(current)
    # 새로 찾은 정점이 없었다면 직전 정점으로 돌아간다
    else:
        current = stack.pop()

print("visit order : ", visited)
