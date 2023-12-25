class LinkedStack:
    class Node:
        def __init__(self, item):
            self.item = item 
            self.next = None 


    def __init__(self):
        self.top = None


    def is_empty(self):
        return self.top is None

    def push(self, new_item):
        newNode = self.Node(new_item)
        newNode.next = self.top
        self.top = newNode

    def pop(self): 
        if self.is_empty():return 'Linked-stack empty on pop'
        else:
            temp = self.top 
            self.top = self.top.next 
            temp.next = None
            del temp 


    def get_top(self):
        if self.is_empty():return 'Linked-stack empty on pop'
        else:
            getTop = self.top.item
            print(getTop)
        

    def display(self):
        cur = self.top 
        while cur is not None: 
            print(cur.item)
            cur = cur.next




if __name__ == '__main__':
    ls = LinkedStack()
    
    ls.push(8)
    ls.push(8)
    ls.push(8)
    ls.push(8)
    ls.push(8)
    ls.push(6)
    ls.push(12)
    ls.get_top()

    # ls.display()