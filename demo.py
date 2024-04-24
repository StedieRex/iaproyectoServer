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
    open_list = [start]
    closed_list = []
    while open_list:
        current = open_list.pop(0)
        if current == goal:
            # Reconstruct path
            path = [goal]
            while current != start:
                current = closed_list[current]['parent']
                path.append(current)
            path.reverse()
            return path

        closed_list.append({current: {'parent': None}})
        for neighbor, data in graph.nodes[current.name].neighbors.items():
            child = neighbor
            child_data = data
            child_g_score = child_data['distance']
            child_h_score = heuristic(child, goal)  # Replace this with a proper heuristic function
            child_f_score = child_g_score + child_h_score

            if not any(child in open_node for open_node in open_list) and not any(child in closed_node for closed_node in closed_list):
                open_list.append(child)
                closed_list.append({child: {'parent': current, 'g_score': child_g_score, 'f_score': child_f_score}})
            elif any(child in open_node for open_node in open_list):
                for node_dict in closed_list:
                    if child in node_dict:
                        existing_g_score = node_dict[child]['g_score']
                        if child_g_score < existing_g_score:
                            node_dict[child]['parent'] = current
                            node_dict[child]['g_score'] = child_g_score
                            node_dict[child]['f_score'] = child_f_score

        open_list.sort(key=lambda node: closed_list[open_list.index(node)][node]['f_score'])

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
