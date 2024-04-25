import math
import time
"""
M es el tamano de dato que enviaremos
"""
M = 100
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

def heuristic(edge_info, parent_node):
    def serverLatency(speed, distance, retransmission):
        s1 = float(M)/float(speed)
        s2 = math.floor(distance/retransmission)
        return s1 + s2
    suma = parent_node.heuristic_value + serverLatency(edge_info['speed'], edge_info['distance'] , edge_info['retransmission'])
    return suma

def a_star_search(graph, start, goal, beam):
    open_set = [start]
    closed_set = []
    counter = 0
    while open_set:
        print(f"open_set={open_set}")
        current_node = open_set.pop(0)
        if current_node == goal:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = current_node.parent
            return path
            
        else:
            # Generate children of current_node

            for neighbor, edge_info in graph.nodes[current_node.name].neighbors.items():
                # print(neighbor)
                if neighbor not in open_set and neighbor not in closed_set:
                    # print("not in open set neitheer close_set")
                    neighbor.parent = current_node
                    # print("current Node")
                    neighbor.heuristic_value = heuristic(edge_info, current_node)
                    # print("heuristic")
                    open_set.append(neighbor)
                    # print("open_set append")
                elif neighbor in open_set:
                    # print("in open Set")
                    # Check if the path to this neighbor from the current node is shorter
                    if neighbor.heuristic_value > heuristic(neighbor, goal):
                        neighbor.parent = current_node
                        neighbor.heuristic_value = heuristic(neighbor, goal)
                # elif neighbor in closed_set:
                #     print("in closed list")
                #     # Check if the path to this neighbor from the current node is shorter
                #     if neighbor.heuristic_value > heuristic(neighbor, goal):
                #         closed_set.remove(neighbor)
                #         open_set.append(neighbor)
        # print("Before close_append")
        closed_set.append(current_node)
        # print("after close_append current node")
        print(closed_set)
        print("\t",[(h, h.heuristic_value) for h in open_set])
        open_set.sort(key=lambda x: x.heuristic_value)
        print("\t",[(h, h.heuristic_value) for h in open_set])
        open_set = open_set[:beam]
        counter += 1
        print(counter)
        time.sleep(2)

    return "FAIL"




# Example usage:
# Assuming graph and nodes are defined elsewhere
# You should also define a heuristic function specific to your problem
# Example usage:
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
graph = Graph()
graph.add_node(node_a)
graph.add_node(node_b)
graph.add_node(node_c)
graph.add_node(node_d)
graph.add_edge(node_a, node_b, speed=10, distance=50, retransmission=2)
graph.add_edge(node_a, node_d, speed=100, distance=50, retransmission=2)
graph.add_edge(node_b, node_c, speed=100, distance=50, retransmission=2)
start_node = node_a
start_node.heuristic_value=0
goal_node = node_c
path = a_star_search(graph, start_node, goal_node, beam=2)
print(path)
