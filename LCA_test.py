import unittest
import LCA
import BTree

class test_lca(unittest.TestCase):

    def test_get_path(self):
        # First construct an arbitrary binary tree
        tree = BTree.BTree(78, BTree.BTree(14), BTree.BTree(9))
        tree.insert_left_node(56)
        tree.insert_right_node(300)
        tree.insert_left_node(164)
        test_path = []
        LCA.get_path(tree, 14, test_path)
        self.assertEqual(test_path, [78, 164, 56, 14], "Should be '[78, 164, 56, 14]'")

        tree = BTree.BTree(1, BTree.BTree(2), BTree.BTree(3))
        tree.get_lt().insert_right_node(4)
        tree.get_rt().insert_left_node(5)
        test_path = []
        LCA.get_path(tree, 5, test_path)
        self.assertEqual(test_path, [1, 3, 5], "Should be '[1, 3, 5]'")
        test_path = []
        LCA.get_path(tree, 4, test_path)
        self.assertEqual(test_path, [1, 2, 4], "Should be '[1, 2, 4]'")

    def test_get_lca(self):
        # First construct an arbitrary binary tree
        tree = BTree.BTree(78, BTree.BTree(14), BTree.BTree(9))
        tree.get_lt().insert_right_node(11)
        tree.get_lt().get_rt().insert_left_node(56)
        tree.get_lt().insert_left_node(300)
        tree.get_lt().get_rt().insert_right_node(164)
        self.assertEqual(LCA.get_LCA(tree, 300, 56), 14, "Should be 14")
        self.assertEqual(LCA.get_LCA(tree, 164, 56), 11, "Should be 11")


if __name__ == '__main__':
    unittest.main()