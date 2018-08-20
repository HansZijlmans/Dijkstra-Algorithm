

class Node():

    def __init__(self, name = ''):
        self.name = name
        self.edges = []
        self.value = 10**100
        self.previous_node = None
        self.active = True
    
    def add_edge(self, edge):
        self.edges.append(edge)

    def __str__(self):
        return f'This is node {self.name} with previous node {self.previous_node} and value {self.value}'

class Edge():

    def __init__(self, connectionA, connectionB, value = "0"):
        self.value = value
        self.nodes = (connectionA, connectionB)

    def __str__(self):
        return f'This edge connects {self.nodes[0]} and {self.nodes[1]} and has a value of {self.value}'

def connect_nodes_edges(graph_nodes, graph_edges):
    for node in graph_nodes.values():

        for edge in graph_edges:

            if node.name == edge.connectionA or node.name == edge.connectionB:
                node.add_edge(edge)

def update_connecting_nodes(graph_nodes, current_node):
    '''
    updates the values for the connecting nodes
    '''
    for edge in current_node.edges:
        if edge.nodes[0] == current_node.name:
            new_node = edge.nodes[1]
        else:
            new_node = edge.nodes[0]
    
        new_value = new_node.value + edge.value

        if new_value > new_node.value:
            new_node.value = new_value
            new_node.previous_node = current_node.name

def find_next_node(graph_nodes):
    '''
    Finds the node with the minimum value
    '''
    
    max_value = 10**100
    
    for node in graph_nodes:

        if node.active and node.value < max_value:
            max_value = node.value
            min_node_name = node.name
    
    if max_value == 10**100:
         raise ValueError('No more nodes available')
    else:
        return graph_nodes[min_node_name]

def list_previous_nodes(graph_nodes, current_node):

    while current_node.previous_node != None:
        print(current_node)
        current_node = graph_nodes[current_node.previous_node]


def dijkstra(graph_nodes, graph_edges):
    starting_node_name = input('Please enter starting node')
    current_node = graph_nodes[starting_node_name]
    ending_node_name = input('Please enter ending node')

    while True:
        try:
            update_connecting_nodes(graph_nodes, current_node)
            current_node.active = False
            current_node = find_next_node(graph_nodes)
        except ValueError:
            break
    
    list_previous_nodes(graph_nodes, graph_nodes[ending_node_name])
    

def main():
    graph_nodes = {'A': Node("A"), 'B': Node("B"), 'C': Node("C"), 'D': Node("D")}
    graph_edges = [Edge('A','B',5), Edge('A','C', 4), Edge('C','D',4)]
    connect_nodes_edges(graph_nodes, graph_edges)
    dijkstra(graph_nodes, graph_edges)    

if __name__ == '__main__':
    main()