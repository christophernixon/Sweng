import unittest
from DAG import DAG


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
        
    def test_delete_node(self):
        dag = DAG()
        dag.add_node('test')
        # Confirm node is added.
        self.assertEqual(dag.graph, {'test': set()}, "Node incorrectly added")
        dag.delete_node('test')
        self.assertEqual(dag.graph, {}, "Is not empty graph when initialised.")

    def test_add_edge(self):
        dag = DAG()
        dag.add_node('1')
        dag.add_node('2')
        dag.add_edge('1', '2')
        self.assertEqual(dag.graph, {'1': set('2'), '2': set()}, "Incorrectly added edge.")


if __name__ == '__main__':
    unittest.main()