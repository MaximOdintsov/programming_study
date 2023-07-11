class Node:
    def __init__(self, value=None, next_node=None, prev_node=None):
        self.next_node = next_node
        self.prev_node = prev_node
        self.value = value

    def __str__(self):
        return str(self.value)


class List:
    """
    Двунаправленный связный список.
    """
    def __init__(self):
        self.top = Node()
        self.tail = self.top

    def append(self, value):
        new_node = Node(value)
        self.tail.next_node = new_node
        new_node.prev_node = self.tail

        self.tail = new_node

    def prepend(self, value):
        """
        Добавление нового элемента в начало двунаправленного списка.
        """

        if self.top.next_node is None:
            self.append(value)
            return

        new_node = Node(value)
        old_next_node = self.top.next_node

        self.top.next_node = new_node

        new_node.next_node = old_next_node
        new_node.prev_node = self.top

        old_next_node.prev_node = new_node

    def __str__(self):
        current = self.top.next_node
        values = ''
        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node
        return f'[{values}]'
