class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

    def print_graph(self):
        for row in self.graph:
            print(row)


# Make Graph
G1 = Graph(4)
G1.graph[0][2] = 1
G1.graph[2][0] = 1
G1.graph[0][3] = 1
G1.graph[3][0] = 1
G1.graph[2][3] = 1
G1.graph[3][2] = 1
G1.graph[1][2] = 1
G1.graph[2][1] = 1

# Print Graph
G1.print_graph()

# Grobal Variable
stack = []
visited = []

# Append Initial Vertex
current = 0
stack.append(current)
visited.append(current)

# Go On A Trip !!
while len(stack):

    next_ = None

    for vertex in range(4):
        if G1.graph[current][vertex] == 1:
            if vertex not in visited:
                next_ = vertex
                break

    # 방문하지 않은 정점이 있다면 일단 방문 한 이후에
    # current 에 방문 지점을 저장하고
    # 현재 위치를 stack 과 visited 에 append 한다
    if next_ is not None:
        current = next_
        stack.append(current)
        visited.append(current)

    # 더이상 방문 할 정점이 없는 경우
    # 스택에 저장되어있는 이전 방문 정점을 pop 해서 current 에 복사한다
    else:
        current = stack.pop()

    # 이전 정점을 current 로 하는 while 반복문을 다시 돈다
    # while 문 시작으로 돌아감

print()
print('visited vertex : ', end=' ')
print(visited)
