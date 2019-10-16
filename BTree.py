"""Class for binary tree, using code from
https://stackoverflow.com/questions/28337989/how-to-build-a-binary-tree-in-python for BTree,
and from https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
for pretty_print()"""
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

    def pretty_print(self):
        lines, _, _, _ = self._pretty_print()
        for line in lines:
            print(line)

    def _pretty_print(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.rt is None and self.lt is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.rt is None:
            lines, n, p, x = self.lt._pretty_print()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.lt is None:
            lines, n, p, x = self.rt._pretty_print()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.lt._pretty_print()
        right, m, q, y = self.rt._pretty_print()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
