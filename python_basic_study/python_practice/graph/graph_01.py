class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


name_arr = ["A", "B", "C", "D"]

G0 = Graph(4)
G0.graph[0][1] = 1
G0.graph[0][2] = 1
G0.graph[0][3] = 1
G0.graph[1][0] = 1
G0.graph[2][0] = 1
G0.graph[3][0] = 1
print("G0")
for r in G0.graph:
    print(r)

# 무방향 그래프 G1
G1 = Graph(4)
G1.graph[0][1] = 1
G1.graph[0][2] = 1
G1.graph[0][3] = 1
G1.graph[1][0] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1
G1.graph[3][0] = 1
G1.graph[3][2] = 1
print("G1")
for r in G1.graph:
    print(r)

# 방향 그래프 G3
G3 = Graph(4)
G3.graph[0][1] = 1
G3.graph[0][2] = 1
G3.graph[3][0] = 1
G3.graph[3][2] = 1
print("G3")
for r in G3.graph:
    print(r)

# 무방향 그래프 G4
G4 = Graph(4)
G4.graph[0][3] = 1
G4.graph[3][0] = 1
G4.graph[3][1] = 1
G4.graph[1][3] = 1
G4.graph[1][2] = 1
G4.graph[2][1] = 1
print("G4")
for r in G4.graph:
    print(r)
