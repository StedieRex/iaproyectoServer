# first search implement using nodes with a parent attribute and children list
# each link has three attributes: distance, velocity, retransmissionDistance
# and a search function that takes a node and a goal and returns the path to the goal

import math

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def add_child(self, child):
        self.children.append(child)

    def search(self, goal):
        if self == goal:
            return [self]
        for child in self.children:
            path = child.search(goal)
            if path:
                return [self] + path
        return None

class Link:
    def __init__(self, node1, node2, distance, velocity, retransmissionDistance):
        self.node1 = node1
        self.node2 = node2
        self.distance = distance
        self.velocity = velocity
        self.retransmissionDistance = retransmissionDistance

    def __str__(self):
        return self.node1.name + " -> " + self.node2.name

    def __repr__(self):
        return self.node1.name + " -> " + self.node2.name

    def get_time(self):
        return self.distance / self.velocity

    def get_retransmissionTime(self):
        return self.retransmissionDistance / self.velocity

    def get_totalTime(self):
        return self.get_time() + self.get_retransmissionTime()

    def get_totalDistance(self):
        return self.distance + self.retransmissionDistance

# def main():
# create nodes
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
i = Node("I")
j = Node("J")
k = Node("K")
l = Node("L")
m = Node("M")
n = Node("N")
o = Node("O")
p = Node("P")
q = Node("Q")
r = Node("R")
s = Node("S")
t = Node("T")
u = Node("U")
v = Node("V")
w = Node("W")
x = Node("X")
y = Node("Y")
z = Node("Z")

# create links
ab = Link(a, b, 1, 1, 0)
ac = Link(a, c, 1, 1, 0)
ad = Link(a, d, 1, 1, 0)
ae = Link(a, e, 1, 1, 0)
af = Link(a, f, 1, 1, 0)
ag = Link(a, g, 1, 1, 0)
ah = Link(a, h, 1, 1, 0)
ai = Link(a, i, 1, 1, 0)
aj = Link(a, j, 1, 1, 0)
ak = Link(a, k, 1, 1, 0)
al = Link(a, l, 1, 1, 0)
am = Link(a, m, 1, 1, 0)
an = Link(a, n, 1, 1, 0)
ao = Link(a, o, 1, 1, 0)
ap = Link(a, p, 1, 1, 0)
aq = Link(a, q, 1, 1, 0)
ar = Link(a, r, 1, 1, 0)
aS = Link(a, s, 1, 1, 0)
