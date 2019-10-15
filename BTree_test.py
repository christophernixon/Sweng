import unittest
import BTree

class test_btree(unittest.TestCase):

    def test_init_tree(self):
        tree = BTree.BTree(11)
        self.assertEqual(tree.get_root(), 11, "Should be 11")
        self.assertEqual(tree.get_lt(), None, "Should be None")
        self.assertEqual(tree.get_rt(), None, "Should be None")
    
    def test_insert_right(self):
        tree = BTree.BTree(11)
        tree.insert_right_node(8)
        self.assertEqual(tree.get_rt().key, 8, "Should be 8")
        tree.insert_right_node(44)
        self.assertEqual(tree.get_rt().key, 44, "Should be 44")

    def test_insert_left(self):
        tree = BTree.BTree(109)
        tree.insert_left_node(105)
        self.assertEqual(tree.get_lt().key, 105, "Should be 105")
        tree.insert_left_node(69)
        self.assertEqual(tree.get_lt().key, 69, "Should be 69")

if __name__ == '__main__':
    unittest.main()