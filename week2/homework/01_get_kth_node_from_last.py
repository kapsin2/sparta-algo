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

    def get_node(self, index):
        node = self.head
        for i in range(index):
            node = node.next
        return node

    def get_kth_node_from_last(self, k):
        cur = self.head
        i = 1
        while cur.next is not None:
            cur = cur.next
            i += 1

        return self.get_node(i - k)


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(3).data) # 7이 나와야 합니다!

