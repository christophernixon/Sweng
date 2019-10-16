import unittest
import LCA
import BTree

class test_lca(unittest.TestCase):

    def test_get_path(self):
        # First construct an arbitrary binary tree
        tree = BTree.BTree(78, 14, 9)
        tree.insert_left_node(56)
        tree.insert_right_node(300)
        tree.insert_left_node(164)
        tree.get_lt().insert_right_node(4)
        tree.get_rt().insert_left_node(5)
        tree.get_rt().get_rt().insert_left_node(1000)
        tree.get_lt().get_lt().get_lt().insert_right_node(99)
        print("\nTesting get_path() for the following tree:\n")
        tree.pretty_print()

        test_path = []
        LCA.get_path(tree, 14, test_path)
        self.assertEqual(test_path, [78, 164, 56, 14], "Should be '[78, 164, 56, 14]'")

        test_path = []
        LCA.get_path(tree, 5, test_path)
        self.assertEqual(test_path, [78, 300, 5], "Should be '[78, 300, 5'")

        test_path = []
        LCA.get_path(tree, 4, test_path)
        self.assertEqual(test_path, [78, 164, 4], "Should be '[78, 164, 4]'")

        test_path = []
        LCA.get_path(tree, 99, test_path)
        self.assertEqual(test_path, [78, 164, 56, 14, 99], "Should be '[78, 164, 56, 14, 99]'")

    def test_get_lca(self):
        # First construct an arbitrary binary tree
        tree = BTree.BTree(0, 1, 2)
        tree.get_lt().insert_right_node(3)
        tree.get_lt().get_rt().insert_left_node(5)
        tree.get_lt().insert_left_node(8)
        tree.get_lt().get_rt().insert_right_node(13)
        tree.get_rt().insert_left_node(21)
        tree.get_rt().insert_right_node(34)
        tree.get_rt().get_rt().insert_left_node(55)
        print("\nTesting get_LCA() for the following tree:\n")
        tree.pretty_print()

        self.assertEqual(LCA.get_LCA(tree, 1, 2), 0, "Should be 0")
        self.assertEqual(LCA.get_LCA(tree, 5, 13), 3, "Should be 3")
        self.assertEqual(LCA.get_LCA(tree, 55, 21), 2, "Should be 2")
        self.assertEqual(LCA.get_LCA(tree, 5, 55), 0, "Should be 0")


if __name__ == '__main__':
    unittest.main()