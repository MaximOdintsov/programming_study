class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class List:
    def __init__(self):
        self.top = Node()
        self.tail = self.top

    def append(self, value):
        self.tail.next_node = Node(value)
        self.tail = self.tail.next_node

    def __str__(self):
        current = self.top.next_node
        values = ''
        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return f'[{values}]'
