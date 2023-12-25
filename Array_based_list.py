class ArrayListType:
    """
    ArrayListType class represents a dynamic array-based implementation of a list.

    Attributes:
        size (int): The maximum size of the array.
        length (int): The current number of elements in the array.
        list (list): The dynamic array to hold the list elements.

    Methods:
        __init__(self, size): Initializes the ArrayListType object with a specified size.
        __del__(self): Destructor to deallocate memory for the array.
        isEmpty(self): Checks if the array is empty.
        isFull(self): Checks if the array is full.
        list_size(self): Returns the current number of elements in the array.
        print_list(self): Prints the elements of the array.
        is_item_at_equal(self, loc, item): Checks if the item at the specified location is equal to a given item.
        insert_at(self, loc, item): Inserts an item at the specified location in the array.
        insert_end(self, item): Inserts an item at the end of the array.
        retrieve_at(self, loc): Retrieves the item at the specified location.
        replace_at(self, loc, item): Replaces the item at the specified location with a new item.
        search(self, item): Searches for the first occurrence of the given item in the array.
        avoid_duplicate(self, item): Inserts an item into the array if it doesn't already exist (no duplicates allowed).
        remove(self, item): Removes the first occurrence of the given item from the array.
        remove_at(self, loc): Removes the item at the specified location from the array.
    """
    def __init__(self, size):
        if size > 0:
            self.size = size
            self.length = 0
            self.list = [0] * self.size
        else:
            print("Size must be greater than 0.")


    def __del__(self):
        del self.list

    def isEmpty(self):
        return self.length == 0
    
    def isFull(self):
        return self.length == self.size
    
    def list_size(self):
        return self.length
    
    def print_list(self):
        for i in range(self.length): 
            print(i)
        print()

    def is_item_at_equal(self, loc, item):
        if 0 <= loc < self.length:
            return self.list[loc] == item
        return False
        

    def insert_at(self, loc, item):
        if self.isFull(): 
            print('List is Full')
        if loc < 0 or loc > self.length: 
            print('Out of range') 

        else: 
            self.list.insert(loc, item)
            self.length += 1


    def insert_end(self, item): 
        if self.isFull(): 
            print('List is Full')
        else:
            self.list[self.length] = item
            self.length += 1


    def retrieve_at(self, loc): 
        if 0 <= loc < self.length:
            return self.list[loc]
        else:
            print("Out of Range")



    def replace_at(self, loc, item): 
        if 0 <= loc < self.length:
            self.list[loc] = item
        else:
            print("Out of Range")
            


    def search(self, item):
        for loc in range(self.length):
            if self.list[loc] == item:
                return loc
        return -1
    

    def avoid_duplicate(self, item): 
        if self.isFull():
            print('The List is Full')

        else: 
            search = self.search(item)
            if search == -1: 
                self.list[self.length] = item
                self.length += 1
            else:
                print("No duplicates are allowed")




    def remove(self, item):
        loc = self.search(item)
        if loc == -1:
            print("The item to be deleted is not in the list")
        else:
            self.remove_at(loc)



    def remove_at(self, loc):
        if 0 <= loc < self.length:
            del self.list[loc]
            self.length -= 1
        else:
            print("The location of the item to be removed is out of range")




def main(): 
    ls = ArrayListType(50)
    for i in range(50): 
        ls.insert_at(i,i)


    ls.print_list()


if __name__ == '__main__': 
    main()