class Stack:
    def __init__(self, array_size):
        self.array_size = array_size
        self.top = -1
        self.item = [None] * self.array_size


    def is_empty(self):
        return self.top < 0
    
    def push(self, element):
        if self.top >= self.array_size - 1:
            return ' Stack full on push'
        

        else :
            self.top += 1
            self.item[self.top] = element


    def pop(self):
        if self.is_empty():
            return 'Stack empty on pop'
        
        else : 
            self.top -= 1


    def pop_element(self):
        if self.is_empty():
            return 'Stack empty on pop'
        
        else: 
            element = self.item[self.top]
            self.top -= 1
            return element
        


    def get_top(self):
        if self.is_empty():
            return 'Stack empty on pop'
        
        else: 
            Stack_top = self.item[self.top]
            return Stack_top
        

    def print_stack(self):
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











