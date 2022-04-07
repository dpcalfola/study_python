# Node
class Node():
    def __init__(self):
        self.data = None
        self.link = None


# Print punction
def print_nodes(start):
    current_i = start
    if current_i is None:
        return
    print(current_i.data, end=" ")
    while current_i.link is not None:
        current_i = current_i.link
        print(current_i.data, end=" ")


# Global variable
memory = []
head, current, pre = None, None, None
data_array = ['Clarkson', 'Anderson', 'Randle', 'D\'russell', 'Ingram', 'Kuzma', 'Caruso']

node = Node()
node.data = data_array[0]
head = node
memory.append(node)

# [1:] - It means data is going to start from the second element
for data in data_array[1:]:
    pre = node  # Copy node to pre
    node = Node()  # Initialize node
    node.data = data  # Save data to the new node
    pre.link = node  # Former node points to the new node
    memory.append(node)

print_nodes(head)
