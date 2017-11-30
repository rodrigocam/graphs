from pythonds.graphs import Graph, Vertex, PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt

def minimum_spanning_tree(graph, initial_city):
    start_city = graph.getVertex(initial_city)
    heap = PriorityQueue()
    aux_list = []
    solution = []
    visited_nodes = []

    new_graph = Graph()

    for conect in start_city.getConnections():
        aux_list.append((start_city.getWeight(conect), (start_city.id, conect.id)))
        visited_nodes.append(start_city.id)

    heap.buildHeap(aux_list)

    while not heap.isEmpty():
        cur_pair = heap.delMin()
        cur_node = graph.getVertex(cur_pair[1])
        
        if cur_node not in visited_nodes:
            solution.append(cur_pair)
            visited_nodes.append(cur_node.id)
            for conect in cur_node.getConnections():
                if conect.id not in visited_nodes:
                    heap.add((cur_node.getWeight(conect), (cur_node.id, conect.id)))
        else:
            continue

    print('Solution: ' + str(solution))

    for city_1, city_2 in solution:
        new_graph.addEdge(city_1, city_2, 0)

    return new_graph

def show_graph(graph, graph_name):
    visible_graph = nx.Graph()

    for city in graph:
        for conect in city.getConnections():
            visible_graph.add_edge(city.id, conect.id)
            visible_graph.add_node(city.id)

    nx.draw_networkx(visible_graph, with_labels=True)
    plt.savefig(graph_name)
    plt.show()