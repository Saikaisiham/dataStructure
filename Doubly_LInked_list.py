class Node:
    def __init__(self, item) -> None:
        """
        Initialize a new node in a doubly linked list.

        Parameters:
        - item: The value of the node.

        Attributes:
        - item: The value of the node.
        - next: Reference to the next node in the list.
        - previous: Reference to the previous node in the list.
        """
        self.item = item
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self) -> None:
        """
        Initialize an empty doubly linked list.

        Attributes:
        - head: Reference to the first node in the list.
        - tail: Reference to the last node in the list.
        - count: The number of nodes in the list.
        """
        self.head = None
        self.tail = None
        self.count = 0

    def insert_head(self, item):
        new_node = Node(item)

        if self.count == 0:
            self.head = self.tail = new_node
            new_node.next = None
            new_node.previous = None
        else:
            new_node.next = self.head
            new_node.previous = None
            self.head.previous = new_node
            self.head = new_node
        self.count += 1

    def insert_tail(self, item):
        new_node = Node(item)

        if self.count == 0:
            self.head = self.tail = new_node
            new_node.previous = new_node.next = None

        else:
            new_node.previous = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def insert_at(self, position, item):
        if position < 0 or position > self.count:
            print('Out of range')

        else:
            new_node = Node(item)
            if position == 1:
                self.insert_head(item)
            if position == self.count:
                self.insert_tail(item)

            else:
                current = self.head
                for i in range(1, position):
                    current = current.next

                new_node.next = current.next
                new_node.previous = current
                current.next.previous = new_node
                current.next = new_node
                self.count += 1

    def remove_head(self):
        if self.count == 0:
            raise AssertionError('Empty List')

        if self.count == 1:
            del self.head
            self.tail = self.head = None

        else:
            current = self.head
            self.head = self.head.next
            self.head.previous = None
            del current

        self.count -= 1

    def remove_tail(self):
        if self.count == 0:
            raise AssertionError('Empty List')

        if self.count == 1:
            del self.head
            self.tail = self.head = None

        else:
            current = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            del current

        self.count -= 1

    def remove_nth_node(self, position):
        if position < 0 or position >= self.count:
            print('Out of Range')

        if position == 0:
            self.remove_head()

        if position == self.count - 1:
            self.remove_tail()

        else:
            current = self.head.next
            for i in range(1, position):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev

            del current

        self.count -= 1

    def print_list(self):
        """
        Print the items in the doubly linked list.

        If the list is empty, it prints "Empty List".
        Otherwise, it iterates through the list and prints each item.
        """
        if self.count == 0:
            print('Empty List')

        else:
            current = self.head
            while current is not None:
                print(current.item)
                current = current.next

        print()


if __name__ == '__main__':
    dl = DoublyLinkedList()
    dl.insert_at(0, 4)
    dl.insert_at(1, 6)
    dl.insert_at(2, 7)
    dl.insert_head(2)
    dl.insert_tail(10)

    dl.print_list()
