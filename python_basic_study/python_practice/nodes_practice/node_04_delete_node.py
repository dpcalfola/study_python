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

# Delete Node
# Copy link from the delete node to before one
# And delete the node
node_2.link = node_3.link
del node_3

current = node_1
print(current.data)

while current.link is not None:
    current = current.link
    print(current.data)
