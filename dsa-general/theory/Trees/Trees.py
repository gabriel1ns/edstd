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

    def __r_contains(self,current_node,value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self,value):
        return self.__r_contains(self.root,value)
    

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    
    def _r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left,value)
        if value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                subtree_min = self.min_value(current_node.right)
                current_node.value = subtree_min
                current_node.right = self.__delete_node(current_node.right, subtree_min)
        return current_node
    
    def delete_node(self, value):
        self.root = self.__delete_node(self.root,value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    

tree = BinarySearchTree()
tree._r_insert(2)
tree._r_insert(1)
tree._r_insert(3)

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)

tree.delete_node(2)

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right)
