"""
General Definitions:
    - Full Tree: Every Node points to 0 or 2 nodes.
    - Perfect: Any level on the tree that has any nodes is completely filled.
    - Complete: Filling the tree from left to right with no gaps.

If a node has more then one parent, it's not a tree.
Nodes that have the same parent Node are called Siblings.
A node that has no children is called a Leaf.
"""

#Binary-Search Trees

"""
Lets do a quick comparison regarding the Big O Notation for the following methods in Trees x Linked Lists:
 - lookup(): O(log(n)) x O(n)
 - remove(): O(log(n)) x O(n)
 - insert(): O(log(n)) x O(1)
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
            self.root = None
    
    """
    We could've defined its root as the first node that we will insert:
    
    class BinarySearchTree:
        def __init__(self,value):
            new_node = Node(value)
            self.root = new_node
    """

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root

        while (True):
            if new_node.value == temp.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self,value):
        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        
        return False

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)


print(f"The root is {my_tree.root.value}")
print(f"The element to the left is {my_tree.root.left.value}")
print(f"The element to the right of the root is {my_tree.root.right.value}")
print(f"The tree contains the number 7: {my_tree.contains(3)}")