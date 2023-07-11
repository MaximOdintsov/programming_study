class Node:
    def __init__(self, value=None, next_node=None):
        self.next_node = next_node
        self.value = value

    def __str__(self):
        return str(self.value)


class SortedList:
    """
    Сортированный связный список.
    """

    def __init__(self, value=None, next_node=None):
        self.top = Node()
        self.next_node = next_node
        self.value = value

    def append(self, value):
        """
        Добавление нового элемента в сортированный однонаправленный список.
        Время работы O(N).
        """
        current = self.top.next_node
        new_node = Node(value)
        if not current:
            self.top.next_node = new_node
            return

        while current.next_node and current.next_node.value > new_node.value:
            current = current.next_node

        if current.value > new_node.value:
            current.next_node, new_node.next_node = new_node, current.next_node
        else:
            self.top.next_node, new_node.next_node = new_node, self.top.next_node

    def __str__(self):
        """
        Возвращает все элементы связного списка в виде строки.
        """
        current = self.top.next_node
        values = ''

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return f'[{values}]'
