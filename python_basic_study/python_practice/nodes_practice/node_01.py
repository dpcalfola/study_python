class Node:
    def __init__(self):
        self.data = None
        self.link = None


node_1 = Node()
node_1.data = "S.Curry"

node_2 = Node()
node_2.data = "J.Poole"
node_1.link = node_2

node_3 = Node()
node_3.data = "J.Clarkson"
node_2.link = node_3

node_4 = Node()
node_4.data = "GP.2"
node_3.link = node_4

print(node_1.data)
print(node_1.link.data)
print(node_1.link.link.data)
print(node_1.link.link.link.data)
