import GraphUtil.Grapher as Graph
import matplotlib.pyplot as plt

if __name__ == "__main__":
    G = Graph.GraphCreation("src/rutas.txt")

    input_source = input("Enter the source: ")
    input_destination = input("Enter the destination: ")

    # Muestra todos los posibles caminos
    Graph.ShowAllDestinations(G, input_source)

    # Encuentra el camino más corto con Dijkstra
    import networkx as nx  # Import the missing package

    shortest_path = Graph.dijkstra_shortest_path(G, input_source, input_destination)
    if shortest_path:
        shortest_path_graph = G.subgraph(shortest_path)
        plt.figure()  # Crear una nueva figura para el segundo gráfico
        nx.draw(shortest_path_graph, with_labels=True, node_color='g', node_size=700)
        plt.title("Shortest Path")
        plt.show()
    else:
        print("No path found.")


    print("Todos los posibles destinos: ")
    Graph.ShowAllDestinations(G, input_source)

    plt.xlim(-1, 1)  # Se puede ajustar según el grafo
    plt.show()
