class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None

    def __str__(self):
        return self.key, self.value


class List:

    def __init__(self):
        self.head = None

    def append(self, key, value):
        if self.head is None:
            self.head = Node(key, value)
            return

        current = self.head
        while current.next_node is not None:
            current = current.next_node

        current.next_node = Node(key, value)

    def find(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next_node
        return None
    

lst = List()
lst.append(1, "A")
lst.append(2, "B")
lst.append(3, "C")
lst.append(4, "D")
print(lst.find(1))
print(lst.find(3))
print(lst.find(5))