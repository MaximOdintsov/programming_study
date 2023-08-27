class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class Stack:

    def __init__(self):
        self.top = Node(None)

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        node = self.top.next_node
        if node:
            self.top.next_node = node.next_node
            return node.value
        return None

    def push(self, value):
        """
        Извлекает элемент со значением value в стек.
        """
        old_node = self.top.next_node
        new_node = Node(value)
        self.top.next_node, new_node.next_node = new_node, old_node


stack = Stack()
stack.push(7)
stack.push(6)
stack.push(2)
stack.push(1)
print(stack.pop())
