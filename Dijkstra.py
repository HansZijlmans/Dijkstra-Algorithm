

class Node():

    def __init__(self, name = ''):
        self.name = name
        self.edges = []
        self.dijkstra_value = 10**10
    
    def add_edge(self, edge):
        self.edges.append(edge)


class Edge():

    def __init__(self, connectionA, connectionB, value = "0"):
        self.value = value
        self.connectionA = connectionA
        self.connectionB = connectionB

    def __str__(self):
        return f'This edge connects {self.connectionA} and {self.connectionB} and has a value of {self.value}'

def connect_nodes_edges(graph_nodes, graph_edges):
    for node in graph_nodes.values():

        for edge in graph_edges:

            if node.name == edge.connectionA or node.name == edge.connectionB:
                node.add_edge(edge)
    
def dijkstra(graph_nodes, graph_edges):
    starting_node_name = input('Please enter starting node')
    starting_node = graph_nodes[starting_node_name]
    for edge in starting_node.edges:
        print(edge)

def main():
    graph_nodes = {'A': Node("A"), 'B': Node("B"), 'C': Node("C"), 'D': Node("D")}
    graph_edges = [Edge('A','B',5), Edge('A','C', 4), Edge('C','D',4)]
    connect_nodes_edges(graph_nodes, graph_edges)
    dijkstra(graph_nodes, graph_edges)
    

if __name__ == '__main__':
    main()