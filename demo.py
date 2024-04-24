class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}  # Dictionary to store neighbors and edge information
        self.parent = None  # Parent node in the path
        self.heuristic_value = 0  # Heuristic value for A* search

    def add_neighbor(self, neighbor, speed, distance, retransmission):
        self.neighbors[neighbor] = {'speed': speed, 'distance': distance, 'retransmission': retransmission}

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return self.name

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

def heuristic(node, parent_node):
    # This is a simple heuristic function. You can replace it with a more sophisticated one if needed.
    return 0

def a_star_search(graph, start, goal):
    import pudb; pudb.set_trace()
    open_set = [start]
    closed_set = []
    while open_set:
        current_node = open_set.pop(0)
        if current_node == goal:
            # Reconstruct path
            path = [current_node]
            while current_node != start:
                for neighbor, _ in graph.nodes[current_node].neighbors.items():
                    if graph.nodes[neighbor.name].parent == current_node:
                        path.insert(0, neighbor)
                        current_node = neighbor
                        break
            return path
        else:
            # Generate children of current_node
            for neighbor, edge_info in graph.nodes[current_node].neighbors.items():
                if neighbor not in open_set and neighbor not in closed_set:
                    neighbor.parent = current_node
                    neighbor.heuristic_value = heuristic(neighbor, goal)
                    open_set.append(neighbor)
                elif neighbor in open_set:
                    # Check if the path to this neighbor from the current node is shorter
                    if neighbor.heuristic_value > heuristic(neighbor, goal):
                        neighbor.parent = current_node
                        neighbor.heuristic_value = heuristic(neighbor, goal)
                elif neighbor in closed_set:
                    # Check if the path to this neighbor from the current node is shorter
                    if neighbor.heuristic_value > heuristic(neighbor, goal):
                        closed_set.remove(neighbor)
                        open_set.append(neighbor)
        closed_set.append(current_node)
        open_set.sort(key=lambda x: x.heuristic_value)

    return "FAIL"




# Example usage:
# Assuming graph and nodes are defined elsewhere
# You should also define a heuristic function specific to your problem
# Example usage:
node_a = Node('A')
node_b = Node('B')
graph = Graph()
graph.add_node(node_a)
graph.add_node(node_b)
graph.add_edge(node_a, node_b, speed=100, distance=50, retransmission=2)
start_node = node_a
goal_node = node_b
path = a_star_search(graph, start_node, goal_node)
print([node.name for node in path])
