class Queue: 
    """A class representing a queue.

    Attributes:
    - size (int): The maximum size of the queue.
    - front (int): The index of the front element in the queue.
    - rear (int): The index of the rear element in the queue.
    - length (int): The current number of elements in the queue.
    - queue (list): The list used to store the elements of the queue.

    Methods:
    - enqueue(item): Adds an item to the rear of the queue.
    - dequeue(): Removes and returns the item at the front of the queue.
    - display(): Displays all the elements in the queue.
    """
    def __init__(self, size) -> None:
        """Initializes the Queue with the given size."""
        self.size = size 
        self.front = 0 
        self.rear = -1
        self.length = 0 
        self.queue = [None] * size


    def enqueue(self, item):
        """Adds an item to the rear of the queue."""
        if self.length == self.size: 
            raise IndexError('Full queue')
        else: 
            self.rear = (self.rear+1) % self.size
            self.queue[self.rear] = item
            self.size += 1

    def dequeue(self):
        """Removes  the item at the front of the queue"""
        if self.length == 0: 
            raise IndexError('Empty Queue')
        else:
            self.front = (self.front+1) % self.size
            self.length -= 1


    def display(self):
        """Displays all the elements in the queue"""
        for i in self.queue:
            print(i)
        


q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.display()
