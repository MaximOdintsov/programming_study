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

    def insert(self, value, after_value):
        """
        Вставка нового элемента в середину связного списка.
        После значения after_value
        """
        current = self.top.next_node
        while current is not None:
            if current.value == after_value:
                old_next_node = current.next_node

                current.next_node = Node(value)
                new_current = current.next_node
                new_current.next_node = old_next_node

                self.tail = current.next_node
                break
            current = current.next_node

    def __str__(self):
        current = self.top.next_node
        values = ''
        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return f'[{values}]'
