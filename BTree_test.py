import unittest
import BTree

class test_btree(unittest.TestCase):

    def test_init_tree(self):
        tree = BTree.BTree(11)
        self.assertEqual(tree.get_root(), 11, "Should be 11")
        self.assertEqual(tree.get_lt(), None, "Should be None")
        self.assertEqual(tree.get_rt(), None, "Should be None")
    
if __name__ == '__main__':
    unittest.main()