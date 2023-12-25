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

    # ... (rest of the class methods)

def main():
    """
    Main function to demonstrate the usage of the ArrayListType class.
    """
    ls = ArrayListType(50)
    for i in range(50):
        ls.insert_at(i, i)

    ls.print_list()

if __name__ == '__main__':
    main()
