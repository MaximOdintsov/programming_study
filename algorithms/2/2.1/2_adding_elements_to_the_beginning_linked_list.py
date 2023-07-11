class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class List:

    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        current = self.head
        while current.next_node is not None:
            current = current.next_node

        current.next_node = Node(value)

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            bottom = Node(value)
            bottom.next_node = self.head
            self.head = bottom

    def __str__(self):
        current = self.head
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"
