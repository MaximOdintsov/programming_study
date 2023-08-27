class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return self.value


class Stack:
    """
    Стек на базе связного списка.
    """
    def __init__(self):
        self.top = Node(None)

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        # Получаем верхний элемент
        top = self.top.next_node

        # Перестраиваем связи и возвращаем значение
        if top:
            self.top.next_node = top.next_node
            return top.value

    def push(self, value):
        """
        Извлекает элемент со значением value в стек.
        """
        # Добавляем элемент в начало связного списка
        new_node = Node(value)

        new_node.next_node = self.top.next_node
        self.top.next_node = new_node

    def clear(self):
        """
        Очищает стек.
        """
        node = self.top.next_node
        while node:
            self.top.next_node = node.next_node
            node = self.top.next_node

    def peek(self):
        """
        Возвращает значение верхнего элемента без его извлечения из стека.
        """
        node = self.top.next_node
        if node:
            return node.value

    def count(self):
        """
        Возвращает количество элементов в стеке.
        """
        node = self.top.next_node
        count = 0
        while node:
            count += 1
            node = node.next_node
        return count


# stack = Stack()
# stack.push(12)
# stack.push(7)
# stack.push(6)
# stack.push(0)
# stack.push(-100000)
# print(stack.peek())
# print(stack.count())
# stack.clear()
# print(stack.count())
# print(stack.peek())