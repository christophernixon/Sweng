import unittest
import BTree

class test_btree(unittest.TestCase):

    def test_init_tree(self):
        tree = BTree.BTree(11)
        self.assertEqual(tree.get_root(), 11, "Should be 11")
        self.assertEqual(tree.get_lt(), None, "Should be None")
        self.assertEqual(tree.get_rt(), None, "Should be None")
        tree = BTree.BTree(7, 8, 9)
        self.assertEqual(tree.get_root(), 7, "Should be 7")
        self.assertEqual(tree.get_lt(), 8, "Should be 8")
        self.assertEqual(tree.get_rt(), 9, "Should be 9")
    
    def test_insert_right(self):
        tree = BTree.BTree(11)
        tree.insert_right_node(8)
        self.assertEqual(tree.get_rt().key, 8, "Should be 8")
        tree.insert_right_node(44)
        tree.get_rt().insert_right_node(9)
        self.assertEqual(tree.get_rt().key, 44, "Should be 44")
        self.assertEqual(tree.get_rt().get_rt().key, 9, "Should be 9")
        self.assertEqual(tree.get_rt().get_rt().get_rt().key, 8, "Should be 8")

    def test_insert_left(self):
        tree = BTree.BTree(109)
        tree.insert_left_node(105)
        self.assertEqual(tree.get_lt().key, 105, "Should be 105")
        tree.insert_left_node(69)
        tree.get_lt().insert_left_node(12)
        self.assertEqual(tree.get_lt().key, 69, "Should be 69")
        self.assertEqual(tree.get_lt().get_lt().key, 12, "Should be 12")
        self.assertEqual(tree.get_lt().get_lt().get_lt().key, 105, "Should be 105")

if __name__ == '__main__':
    unittest.main()