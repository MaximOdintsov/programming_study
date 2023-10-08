class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return self.value


class Queue:
    """
    Очередь на базе двунаправленного связного списка.
    """

    def __init__(self):
        self.top = Node(None)
        self.first = None

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        new_node = Node(value=value)

        if self.first is None:
            self.first = new_node
        if self.top.next_node is not None:
            self.top.next_node.prev_node = new_node

        new_node.next_node = self.top.next_node
        new_node.prev_node = self.top
        self.top.next_node = new_node

        return new_node

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """
        first = self.first
        self.first = first.prev_node
        return first.value


queue = Queue()
queue.enqueue(7)
queue.enqueue(6)
queue.enqueue(2)
queue.enqueue(1)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(13)