import DAG

def get_LCA_DAG(dag: DAG, node_a, node_b):
    # Check DAG is not null
    if not dag:
        return set()

    # Check DAG is valid(should already be but just to be sure)
    if not dag.validate():
        return set()

    # Check dag is empty
    if dag.size() == 0:
        return set()

    if node_a == node_b:
        return set(dag.predecessors(node_a))

    # Calculate ind_nodes
    ind_nodes = set(dag.ind_nodes())

    if node_a in ind_nodes and node_b in ind_nodes:
        return set()
    elif node_a in ind_nodes:
        return set(node_a)
    elif node_b in ind_nodes:
        return set(node_b)

    else:
        predecessors_a = set([node_a])
        predecessors_b = set([node_b])

        while predecessors_a.intersection(predecessors_b) == set():

            for tmp_node in predecessors_a.copy():
                predecessors_a = predecessors_a.union(set([pred for pred in dag.predecessors(tmp_node)]))
            for tmp_node in predecessors_b.copy():
                predecessors_b = predecessors_b.union(set([pred for pred in dag.predecessors(tmp_node)]))

        return predecessors_a.intersection(predecessors_b)

