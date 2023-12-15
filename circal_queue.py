class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.array = [None] * self.max_size
        self.front = 0
        self.rear = self.max_size - 1
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.max_size

    def enqueue(self, element):
        if self.isFull(): 
            print("Queue Full Can't Enqueue ...!")
        else:
            self.rear = (self.rear + 1) % self.max_size
            self.array[self.rear] = element
            self.count += 1

    def dequeue(self):
        if self.isEmpty():
            print('Empty Queue!')
        else:
            self.front = (self.front + 1) % self.max_size
            self.count -= 1  

    def get_front(self):
        assert not self.isEmpty()
        return self.array[self.front]

    def get_rear(self):
        assert not self.isEmpty()
        return self.array[self.rear]

    def search(self, element):
        pos = -1
        for i in range(self.front, self.rear + 1):  
            if self.array[i] == element:
                pos = i
                break

        return pos

    def print_queue(self):
        if not self.isEmpty():
            for i in range(self.front, self.rear + 1): 
                print(self.array[i], end=" ")
            print()
        else:
            print("Empty Queue")


q = Queue(5)
q.enqueue(6)
q.enqueue(8)
q.enqueue(9)
q.enqueue(4)
q.enqueue(3)
q.dequeue()
print(q.get_front())
q.print_queue()

