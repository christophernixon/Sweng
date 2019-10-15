"""Class for binary tree, using code from
https://stackoverflow.com/questions/28337989/how-to-build-a-binary-tree-in-python"""
class BTree:
    def __init__(self, key, left_tree=None, right_tree=None):
        self.key = key
        self.lt = left_tree
        self.rt = right_tree
    
    def insert_right_node(self, node):
        if self.rt == None:
            self.rt = BTree(node)
        else:
            # Create new tree and insert it into appropriate place.
            t = BTree(node)
            self.rt = t
    
    def insert_left_node(self, node):
        if self.lt == None:
            self.lt = BTree(node)
        else:
            # Create new tree and insert it into appropriate place.
            t = BTree(node)
            self.lt = t
    
    # Getters and Setters
    def get_rt(self):
                return self.rt

    def get_lt(self):
            return self.lt
    
    def set_root(self, val):
                self.key = val

    def get_root(self):
            return self.key