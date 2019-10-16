"""Initial approach will be using simple algorithm: for finding LCA of n1 and n2,
the path from root to n1 and root to n2 will be found and stored in two separate arrays.
Both these arrays will be traversed similtaniously until a node with a differing key is found.
This node will then be returned as the LCA."""
import BTree

def get_path(root, key, path):
    # Base Case
    if root is None: 
        return False

    # Add this node's key to path
    path.append(root.key)

    # Check if it is desired node
    if root.key == key: 
        return True

    # If not desired node, check left and right sub-tree
    if root.lt != None and get_path(root.lt, key, path):
        return True 
    if root.rt != None and get_path(root.rt, key, path):
        return True
    
    # If this point is reached, then desired node is not in left or right subtree
    path.pop()
    return False

# Returns LCA if nodes node1, node2 are in the given binary tree, else returns -1 
def get_LCA(root, node1, node2):
    # Initialise paths
    path1 = []
    path2 = []

    if not get_path(root, node1, path1): 
        return -1
    if not get_path(root, node2, path2): 
        return -1

    # Simple while loop comparing nodes in path until nodes differ.
    i = 0 
    while(i < len(path1) and i < len(path2)): 
        if path1[i] != path2[i]: 
            break
        i += 1
    return path1[i-1] 
