class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def verify_binary_tree(root):
    if root is None:
        return True, "Empty tree is valid"
    
    visited = {}
    
    def dfs(node, parent=None):
        node_id = id(node)
        if node_id in visited:
            return False, "Cycle detected in structure"
        
        visited[node_id] = True
        
        children = 0
        if node.left is not None:
            children += 1
        if node.right is not None:
            children += 1
        
        if children > 2:
            return False, f"Node {node.value} has more than 2 children"
        
        if node.left is not None:
            valid, msg = dfs(node.left, node)
            if not valid:
                return False, msg
        
        if node.right is not None:
            valid, msg = dfs(node.right, node)
            if not valid:
                return False, msg
        
        return True, ""
    
    valid, message = dfs(root)
    
    if valid:
        return True, "Valid binary tree"
    else:
        return False, message