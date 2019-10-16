"""Class for binary tree, using code from
https://stackoverflow.com/questions/28337989/how-to-build-a-binary-tree-in-python"""
class BTree:
    def __init__(self, key, left_tree=None, right_tree=None):
        self.key = key
        self.lt = left_tree
        self.rt = right_tree
    
    def insert_right_node(self, key):
        if self.rt == None:
            self.rt = BTree(key)
        else:
            # Create new tree and insert it into appropriate place.
            t = BTree(key)
            t.rt = self.rt
            self.rt = t
    
    def insert_left_node(self, node):
        if self.lt == None:
            self.lt = BTree(node)
        else:
            # Create new tree and insert it into appropriate place.
            t = BTree(node)
            t.lt = self.lt
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

# class Node:
#     def __init__(self, key, left_node=None, right_node=None):
#         self.key = key
#         self.ln = left_tree
#         self.rn = right_tree
    
#     def get_rn(self):
#                 return self.rn

#     def get_ln(self):
#             return self.ln