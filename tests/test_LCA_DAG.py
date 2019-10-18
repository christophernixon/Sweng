import unittest
import LCA_DAG
from DAG import DAG

class test_lca_dag(unittest.TestCase):
    def test_get_lca(self):
        # Empty graph
        dag = DAG()
        self.assertEqual(LCA_DAG.get_LCA_DAG(dag, '1', '2'), (), "Should be empty set.")

        # Single node graph
        dag = DAG()
        dag.add_node('1')
        self.assertEqual(LCA_DAG.get_LCA_DAG(dag, '1', '2'), (), "Should be empty set.")

        # Test single edge, two node graph
        dag = DAG()
        dag.add_node('1')
        dag.add_node('2')
        dag.add_edge('1', '2')
        self.assertEqual(LCA_DAG.get_LCA_DAG(dag, '1', '2'), ('1'), "Should be 1 as nodes are considered their own ancestors.")

        # Test more complicated graph
        dag = DAG()
        dag.add_node('1')
        dag.add_node('2')
        dag.add_node('3')
        dag.add_node('4')
        dag.add_edge('1', '2')
        dag.add_edge('1', '3')
        dag.add_edge('2', '3')
        dag.add_edge('3', '4')
        self.assertEqual(LCA_DAG.get_LCA_DAG(dag, '1', '2'), ('1'), "Should be 1.")
        self.assertEqual(LCA_DAG.get_LCA_DAG(dag, '1', '3'), ('1'), "Should be 1.")
        self.assertEqual(LCA_DAG.get_LCA_DAG(dag, '1', '4'), ('1'), "Should be 1.")
        self.assertEqual(LCA_DAG.get_LCA_DAG(dag, '2', '3'), ('2'), "Should be 2.")
        self.assertEqual(LCA_DAG.get_LCA_DAG(dag, '2', '4'), ('2'), "Should be 2.")
        self.assertEqual(LCA_DAG.get_LCA_DAG(dag, '3', '4'), ('3'), "Should be 3.")

        # Test different, slightly complicated graph
        dag = DAG()
        dag.add_node('A')
        dag.add_node('B')
        dag.add_node('C')
        dag.add_node('D')
        dag.add_node('E')
        dag.add_node('F')
        dag.add_node('G')
        dag.add_edge('G', 'D')
        dag.add_edge('G', 'F')
        dag.add_edge('F', 'E')
        dag.add_edge('E', 'B')
        dag.add_edge('D', 'C')
        dag.add_edge('C', 'B')
        dag.add_edge('B', 'A')
        self.assertEqual(LCA_DAG.get_LCA_DAG(dag, 'C', 'E'), ('B'), "Should be B.")
        self.assertEqual(LCA_DAG.get_LCA_DAG(dag, 'D', 'E'), ('B'), "Should be B.")

if __name__ == '__main__':
    unittest.main()