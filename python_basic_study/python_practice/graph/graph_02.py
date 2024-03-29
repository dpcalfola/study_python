class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


G0 = Graph(4)
G0.graph[0][3] = 1
G0.graph[3][0] = 1
G0.graph[0][2] = 1
G0.graph[2][0] = 1
G0.graph[2][3] = 1
G0.graph[3][2] = 1
G0.graph[1][2] = 1
G0.graph[2][1] = 1

for r in G0.graph:
    print(r)

stack = []
visited_arr = []


def print_status():
    print("stack : ", stack)
    print("visited_arr : ", visited_arr)
    print("next : ", next_)
    print("current : ", current)
    print()


# DFS 시작


# Start Vertex
current = 0
stack.append(current)
visited_arr.append(current)

# Visit next vertex (result : visit 2)
next_ = None
for vertex in range(4):
    # [*][] == departure point
    # [][*] == arrival
    if G0.graph[current][vertex] == 1:
        next_ = vertex
        break
current = next_
stack.append(current)
visited_arr.append(current)
print_status()

# Visit next vertex (result : visit 1)
next_ = None
for vertex in range(4):
    if G0.graph[current][vertex] == 1:
        if vertex in visited_arr:
            pass
        else:
            next_ = vertex
            break
current = next_
stack.append(current)
visited_arr.append(current)
print_status()

# Get back process
next_ = None
for vertex in range(4):
    if G0.graph[current][vertex] == 1:
        if vertex in visited_arr:
            pass
        else:
            next_ = vertex
            break
# 정점에 방문 했을 경우 => next_ 에 값이 있다.
if next_ is not None:
    current = next_
    stack.append(current)
    visited_arr.append(current)
else:
    current = stack.pop()
print_status()
