class Node:
    def __init__(self, data=None):
        self.data = data 
        self.next = None
    def __repr__(self) -> str:
        return f"Node data:{self.data}"
        


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if not self.head:
            self.head = Node(data)
        else: 
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data) 

    def __repr__(self) -> str:
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return '->'.join(nodes)    


L1 = LinkedList()
L1.add(1)
L1.add(2)
L1.add(5)


print(L1)