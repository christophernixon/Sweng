import unittest
from DAG import DAG, DAGValidationError


class test_dag(unittest.TestCase):
    
    def test_init(self):
        dag = DAG()
        self.assertIsNot(dag, None)
        self.assertEqual(dag.graph, {}, "Is not empty graph when initialised.")

    def test_add_node(self):
        dag = DAG()
        dag.add_node('test')
        self.assertEqual(dag.graph, {'test': set()}, "Node incorrectly added")
        dag.add_node('second_test')
        self.assertEqual(dag.graph, {'test': set(), 'second_test': set()}, "Second node incorrectl added")
        
    def test_add_edge(self):
        dag = DAG()
        dag.add_node('1')
        dag.add_node('2')
        dag.add_edge('1', '2')
        self.assertEqual(dag.graph, {'1': set('2'), '2': set()}, "Incorrectly added edge.")

    def test_delete_node(self):
        dag = DAG()
        dag.add_node('test')
        # Confirm node is added.
        self.assertEqual(dag.graph, {'test': set()}, "Node incorrectly added")
        dag.delete_node('test')
        self.assertEqual(dag.graph, {}, "Is not empty graph when initialised.")

        dag = DAG()
        dag.add_node('1')
        dag.add_node('2')
        dag.delete_node('2')
        self.assertEqual(dag.graph, {'1': set()}, "Node '2' incorrectly deleted.")

    def test_delete_edge(self):
        dag = DAG()
        dag.add_node('1')
        dag.add_node('2')
        dag.add_edge('1', '2')
        # Confirm edge is added.
        self.assertEqual(dag.graph, {'1': set('2'), '2': set()}, "Incorrectly added edge.")
        dag.delete_edge('1', '2')
        self.assertEqual(dag.graph, {'1': set(), '2': set()}, "Incorrectly deleted edge.")

        # Test deleting single edge from node with multiple edges.
        dag.add_edge('1', '2')
        dag.add_node('3')
        dag.add_edge('1', '3')
        dag.delete_edge('1', '2')
        self.assertEqual(dag.graph, {'1': set('3'), '2': set(), '3': set()}, "Incorrectly deleted edge.")

    def test_ind_nodes(self):
        dag = DAG()
        dag.add_node('1')
        dag.add_node('2')
        dag.add_node('3')
        dag.add_node('4')
        dag.add_edge('1', '2')
        dag.add_edge('1', '3')
        dag.add_edge('2', '3')
        dag.add_edge('3', '4')
        self.assertEqual(dag.ind_nodes(), ['1'], "Only independant node should be 1.")

        # Test that graph with single node returns one node as independant.
        dag = DAG()
        dag.add_node('9')
        self.assertEqual(dag.ind_nodes(), ['9'], "Only independant node should be 9.")

        # Test empty graph
        dag = DAG()
        self.assertEqual(dag.ind_nodes(), [], "Independant nodes in an empty graph isn't an empty list.")

    def test_topological_sort(self):
        # Test empty graph
        dag = DAG()
        self.assertEqual(dag.topological_sort(), [], "Incorrect topological sorting")

        # Single node graph
        dag = DAG()
        dag.add_node('1')
        self.assertEqual(dag.topological_sort(), ['1'], "Incorrect topological sorting")

        # Test single edge, two node graph
        dag = DAG()
        dag.add_node('1')
        dag.add_node('2')
        dag.add_edge('1', '2')
        self.assertEqual(dag.topological_sort(), ['1', '2'], "Incorrect topological sorting")

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
        self.assertEqual(dag.topological_sort(), ['1', '2', '3', '4'], "Incorrect topological sorting")

    def test_validate(self):
        # Empty graph
        dag = DAG()
        self.assertEqual(dag.validate(), (False, 'no independent nodes detected'), "Invalid graph incorrectly identified as valid.")

        # Single node graph
        dag = DAG()
        dag.add_node('1')
        self.assertEqual(dag.validate(), (True, 'valid'), "Valid graph incorrectly identified as invalid.")

        # Single edge, two node graph
        dag = DAG()
        dag.add_node('1')
        dag.add_node('2')
        dag.add_edge('1', '2')
        self.assertEqual(dag.validate(), (True, 'valid'), "Valid graph incorrectly identified as invalid.")

        # More complicated graph
        dag = DAG()
        dag.add_node('1')
        dag.add_node('2')
        dag.add_node('3')
        dag.add_node('4')
        dag.add_edge('1', '2')
        dag.add_edge('1', '3')
        dag.add_edge('2', '3')
        dag.add_edge('3', '4')
        self.assertEqual(dag.validate(), (True, 'valid'), "Valid graph incorrectly identified as invalid.")

        # Test that exception is raised whenever edge is added that will cause graph to fail topological sort.
        dag = DAG()
        dag.add_node('1')
        dag.add_node('2')
        dag.add_node('3')
        dag.add_edge('1', '2')
        dag.add_edge('2', '3')
        with self.assertRaises(DAGValidationError):
            dag.add_edge('3', '1')
    
    def test_predecessors(self):
        # Empty graph
        dag = DAG()
        self.assertEqual(dag.predecessors('1'), [], "Incorrect Predecessors")

        # Single node graph
        dag = DAG()
        dag.add_node('1')
        self.assertEqual(dag.predecessors('1'), [], "Incorrect Predecessors")

        # Single edge, two node graph
        dag = DAG()
        dag.add_node('1')
        dag.add_node('2')
        dag.add_edge('1', '2')
        self.assertEqual(dag.predecessors('1'), [], "Incorrect Predecessors")
        self.assertEqual(dag.predecessors('2'), ['1'], "Incorrect Predecessors")

        # Complicated graph
        dag = DAG()
        dag.add_node('1')
        dag.add_node('2')
        dag.add_node('3')
        dag.add_node('4')
        dag.add_edge('1', '2')
        dag.add_edge('1', '3')
        dag.add_edge('2', '3')
        dag.add_edge('3', '4')
        self.assertEqual(dag.predecessors('1'), [], "Incorrect Predecessors")
        self.assertEqual(dag.predecessors('2'), ['1'], "Incorrect Predecessors")
        self.assertEqual(dag.predecessors('3'), ['1', '2'], "Incorrect Predecessors")
        self.assertEqual(dag.predecessors('4'), ['3'], "Incorrect Predecessors")

if __name__ == '__main__':
    unittest.main()