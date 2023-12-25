class Stack:
    """
    Stack class represents a simple stack data structure.

    Attributes:
        array_size (int): The maximum size of the stack.
        top (int): Index of the top element in the stack (-1 for an empty stack).
        item (list): List to store elements in the stack.

    Methods:
        __init__(self, array_size): Initializes a new Stack with the specified array size.
        is_empty(self): Checks if the stack is empty.
        push(self, element): Pushes an element onto the stack.
        pop(self): Pops the top element off the stack without returning it.
        pop_element(self): Pops and returns the top element from the stack.
        get_top(self): Returns the top element of the stack without removing it.
        print_stack(self): Prints the elements of the stack.
    """

    def __init__(self, array_size):
        """
        Initializes a new Stack with the specified array size.

        Parameters:
            array_size (int): The maximum size of the stack.
        """
        self.array_size = array_size
        self.top = -1
        self.item = [None] * self.array_size

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.top < 0

    def push(self, element):
        """
        Pushes an element onto the stack.

        Parameters:
            element: The element to be pushed onto the stack.

        Returns:
            str: 'Stack full on push' if the stack is full, otherwise None.
        """
        if self.top >= self.array_size - 1:
            return ' Stack full on push'
        else:
            self.top += 1
            self.item[self.top] = element

    def pop(self):
        """
        Pops the top element off the stack without returning it.

        Returns:
            str: 'Stack empty on pop' if the stack is empty, otherwise None.
        """
        if self.is_empty():
            return 'Stack empty on pop'
        else:
            self.top -= 1

    def pop_element(self):
        """
        Pops and returns the top element from the stack.

        Returns:
            str: 'Stack empty on pop' if the stack is empty, the popped element otherwise.
        """
        if self.is_empty():
            return 'Stack empty on pop'
        else:
            element = self.item[self.top]
            self.top -= 1
            return element

    def get_top(self):
        """
        Returns the top element of the stack without removing it.

        Returns:
            str: 'Stack empty on pop' if the stack is empty, the top element otherwise.
        """
        if self.is_empty():
            return 'Stack empty on pop'
        else:
            stack_top = self.item[self.top]
            return stack_top

    def print_stack(self):
        """
        Prints the elements of the stack.
        """
        print("[", end=" ")
        for i in range(self.top, -1, -1):
            print(self.item[i], end=" ")
        print("]")



if __name__ == "__main__":
    s = Stack(6)
    s.push(5)
    s.push(15)
    s.push(20)
    s.print_stack()











