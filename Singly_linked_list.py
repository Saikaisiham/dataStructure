class SinglyLinkedList():

    """
    SinglyLinkedList class represents a dynamic linked list.

    Attributes:
        size (int): The maximum size of the list.
        length (int): The current number of nodes in the list.
        head (Node or None): The first Node in the list.
        tail (Node or None): The last Node in the list.

    Methods:
        __init__(self, size): Initializes the SinglyLinkedList object with a specified size.
        insert_head(self, item): Inserts a node at the beginning of the list.
        insert_tail(self, item): Inserts a node at the end of the list.
        insert_at(self, location, item): Inserts a node at the specified location.
        remove_head(self): Removes the first node from the list.
        remove_tail(self): Removes the last node from the list.
        remove_at(self, location): Removes a node at the specified location.
        print_list(self): Prints the elements of the list.
    """


    class Node: 
        """
        Node class represents a node in a singly linked list.

        Attributes:
            item: The data stored in the node.
            next (Node or None): Reference to the next node in the list.

        Methods:
            __init__(self, item): Initializes the Node with the given data.
        """
        def __init__(self, item) -> None:
            self.item = item
            self.next = None

    def __init__(self, size):
        self.size =size
        self.head = None 
        self.tail = None 
        self.length = 0


    def insert_head(self, item): 
        newNode = self.Node(item)
        
        if self.length == 0 :
            self.head = self.tail = newNode
            newNode.next = None

        else : 
            newNode.next = self.head
            self.head = newNode

        self.length += 1


    def insert_tail(self, item): 
        newNode = self.Node(item)
        
        if self.length == 0 :
            self.head = self.tail = newNode
            newNode.next = None

        else:
            self.tail.next = newNode
            newNode.next = None
            self.tail = newNode

        self.length += 1



    def insert_at(self, location, item): 
        if location < 0 or location > self.length: 
            print('Out of range')

        else: 
            newNode = self.Node(item)

            if location == 0 :
                self.insert_head(item)

            elif location == self.length:
                self.insert_tail(item)

            else:
                current = self.head 

                for i in range(1, location):
                    current = current.next


                newNode.next = current.next
                current.next = newNode
                self.length += 1


    def remove_head(self):
        if self.length == 0: 
            print('Empty list')

        elif self.length == 1 : 
            del self.head 
            self.tail = None 
            self.length -= 1


        else : 
            current = self.head 
            self.head = self.head.next
            del current
            self.length -= 1




    def remove_tail(self):
        if self.length == 0 : 
            print('Empty list')

        elif self.length == 1: 
            del self.head 
            self.head = self.tail = None 
            self.length -= 1

        else:
            current = self.head.next
            trail_current = self.head

            while current != self.tail:
                tail_current = current
                current = current.next

            del current
            tail_current.next = None
            self.tail = tail_current
            self.length -= 1 
            

    def remove_at(self, location):
        if location < 0 or location >= self.length:
            print("ERROR: Out of range")
        else:
            current, tail_current = None, None
            if location == 0:
                current = self.head
                self.head = self.head.next
                del current
                self.length -= 1
                if self.length == 0:
                    self.tail = None
            else:
                current = self.head.next
                tail_current = self.head

                for i in range(1, location):
                    tail_current = current
                    current = current.next

                tail_current.next = current.next
                if self.tail == current:
                    self.tail = tail_current

                del current
                self.length -= 1


    def print_list(self):
        current = self.head
        while current is not None : 
            print(current.item)
            current =current.next




if __name__ == '__main__': 
    s = SinglyLinkedList(50)
    for i in range(1,50):
        s.insert_tail(i)


    s.print_list()