class TreeNode:
    def __init__(self, item) -> None:
        """
        Initialize a tree node 

        Args:
            item: THe value to be stored in the node 
        """
        self.item = item
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        """Initialize an empty binary saerch tree"""
        self.root = None

    def isEmpty(self):
        return self.root is None

    def insert(self, item):
        """Insert a new item into the binary search tree.

        Args:
            item: The value to be inserted.

        Notes:
            If the item already exists in the tree, it won't be inserted to avoid duplicates.
        """
        if self.root is None:
            self.root = TreeNode(item)
        else:
            current = self.root
            trailing_current = None

            while current is not None:
                trailing_current = current

                if current.item == item:
                    print('The insert item is already in the list')
                    return  

                if current.item > item:
                    current = current.left
                else:
                    current = current.right

            new_node = TreeNode(item)
            if trailing_current.item > item:
                trailing_current.left = new_node
            else:
                trailing_current.right = new_node

    def delete(self, root, item):
        """Delete an item from the binary search tree.

        Args:
            root: The root of the current subtree.
            item: The value to be deleted.

        Returns:
            TreeNode: The modified root of the subtree after deletion.
        """
        if root is None:
            return root

        if item < root.item:
            root.left = self.delete(root.left, item)
        elif item > root.item:
            root.right = self.delete(root.right, item)
        else:
            
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            
            temp = self.min_value_node(root.right)

            
            root.item = temp.item

           
            root.right = self.delete(root.right, temp.item)

        return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, item):
        """Search for an item in the binary search tree.

        Args:
            item: The value to be searched.

        Returns:
            bool: True if the item is found, False otherwise.
        """
        current = self.root

        while current is not None:
            if current.item == item:
                return True
            elif current.item > item:
                current = current.left
            else:
                current = current.right

        return False

    def search_recursive(self, root, item):
        """Search for an item in the binary search tree using recursion.

        Args:
            root: The root of the current subtree.
            item: The value to be searched.

        Returns:
            bool: True if the item is found, False otherwise.
        """
        if root is None:
            return False
        elif root.item == item:
            return True
        elif root.item > item:
            return self.search_recursive(root.left, item)
        else:
            return self.search_recursive(root.right, item)
