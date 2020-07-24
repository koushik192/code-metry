class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        # Your code goes here
        return self.preorder_search(self.root,find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        s=""
        traversal=self.preorder_print(self.root,[])
        for i in traversal:
            s=s+str(i)
        return r[::-1]

        pass

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start:
            if start.value==find_val:
                return True
            if(start.left==find_val):
                return True
            if(start.right==find_val):
                return True
        return False
        

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        # Your code goes here
        if start:
            traversal.append(start.value)
            if start.left:
                self.preorder_print(start.left,traversal)
            if start.right:
                self.preorder_print(start.right,traversal)
        pass
