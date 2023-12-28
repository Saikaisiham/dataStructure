class Node:
    """
    Represents a node in a binary tree.

    Attributes: 
    -value: The value stored in the code 
    -left: References to the left child node 
    -right: References to the right child in the node
    """
    def __init__(self, value) -> None:
        """
        Initializes a nex instance of the Node class.

        Parameters: 
        -value: THe value to bes dtored in the node .
        """
        self.value = value
        self.left = None
        self.right = None

def post_order(root):
    """
    Preform post-order traversal on binary tree

    Parameters:
    -root: The root node of the binary tree.
    Prints the values of nodes in the order : left subtree, right subtree, root 
    """
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.value)



if __name__ == '__main__': 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 

    post_order(root)