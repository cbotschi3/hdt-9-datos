import heapq
import networkx as nx

def GraphCreation(PathFile: str) -> nx.Graph:
    with open(PathFile, 'r') as f:
        G = nx.Graph()
        for line in f:
            line = line.split(",")
            G.add_edge(line[0], line[1], weight=float(line[2]))  # Convertir el peso a float
    return G 

def dijkstra_shortest_path(G, start, end):
    distances = {node: float('inf') for node in G.nodes()}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        if current_node == end:
            break
        
        for neighbor in G.neighbors(current_node):
            distance = current_distance + G[current_node][neighbor]['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    if distances[end] == float('inf'):
        return None
    
    path = [end]
    current_node = end
    
    while current_node != start:
        for neighbor in G.neighbors(current_node):
            if distances[neighbor] == distances[current_node] - G[current_node][neighbor]['weight']:
                path.append(neighbor)
                current_node = neighbor
                break
    
    path.reverse()
    return path

def ShowAllDestinations(G: nx.Graph, source: str) -> None:
    def dfs_with_graph(G, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not G.has_node(start):
            return []
        paths = []
        for node in G.neighbors(start):
            if node not in path:
                newpaths = dfs_with_graph(G, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def draw_paths(G, paths):
        pos = nx.spring_layout(G)
        for path in paths:
            edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='g', node_size=700)
            nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='g', width=2)
            labels = {node: node for node in path}
            nx.draw_networkx_labels(G, pos, labels=labels)

    all_destinations = G.nodes()
    for destination in all_destinations:
        if destination != source:
            all_paths = dfs_with_graph(G, source, destination)
            if all_paths:
                print(f"All possible paths from {source} to {destination}:")
                for path in all_paths:
                    print(path)
                    draw_paths(G, [path])
