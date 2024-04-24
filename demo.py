import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}  # Dictionary to store neighbors and edge information

    def add_neighbor(self, neighbor, speed, distance, retransmission):
        self.neighbors[neighbor] = {'speed': speed, 'distance': distance, 'retransmission': retransmission}

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def add_edge(self, node1, node2, speed, distance, retransmission):
        if node1.name in self.nodes and node2.name in self.nodes:
            self.nodes[node1.name].add_neighbor(node2, speed, distance, retransmission)
            self.nodes[node2.name].add_neighbor(node1, speed, distance, retransmission)
        else:
            raise ValueError("Nodes not in graph")

def astar(graph, start, goal):
    open_list = [(0, start)]
    closed_list = {}
    g_scores = {node: float('inf') for node in graph.nodes}
    g_scores[start] = 0
    f_scores = {node: float('inf') for node in graph.nodes}
    f_scores[start] = heuristic(start, goal)

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = closed_list.get(current)
            return path[::-1]

        for neighbor, data in graph.nodes[current.name].neighbors.items():
            tentative_g_score = g_scores[current] + data['distance']
            if tentative_g_score < g_scores[neighbor]:
                closed_list[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_scores[neighbor], neighbor))

    return "FAIL"

def heuristic(node, goal):
    # Placeholder heuristic function, you can replace it with actual heuristic calculation
    return 0

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")

    graph.add_node(A)
    graph.add_node(B)
    graph.add_node(C)
    graph.add_node(D)

    graph.add_edge(A, B, 5, 10, 1)
    graph.add_edge(A, C, 3, 8, 0)
    graph.add_edge(B, D, 4, 9, 2)
    graph.add_edge(C, D, 6, 12, 1)

    path = astar(graph, A, D)
    print(path)
