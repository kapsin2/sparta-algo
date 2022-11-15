class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        for i in range(index):
            node = node.next
        return node

    def delete_node(self, index):
        if index == 0:
            self.head = self.get_node(1)
            return

        node = self.get_node(index-1)
        node.next = node.next.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(7)
linked_list.delete_node(2)
linked_list.print_all()