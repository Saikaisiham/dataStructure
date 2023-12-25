class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

class LinkedQueue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def enqueue(self, item):
        newNode = Node(item)
        newNode.next = None

        if self.isEmpty():
            self.rear = self.front = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            print('Empty linked queue')
        elif self.count == 1:
            del self.front
            self.rear = None
            self.count -= 1
        else:
            current = self.front
            self.front = self.front.next
            del current
            self.count -= 1

    def clear_all(self):
        current = self.front
        while current is not None:
            temp = current
            current = current.next
            del temp

        self.rear = None
        self.count = 0

    def display(self):
        current = self.front
        while current is not None:
            print(current.item)
            current = current.next

    def search(self, item):
        current = self.front
        flag = True
        while current is not None:
            if current.item == item:
                print(f'The item {item} found')
                flag = False
                break
            current = current.next

        if flag:
            print(f'The item {item} was not found')

if __name__ == "__main__":
    q1 = LinkedQueue()

    for i in range(1, 21):
        q1.enqueue(i)

    q1.display()
