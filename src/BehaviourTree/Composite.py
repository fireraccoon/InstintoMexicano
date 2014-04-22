"""
* Selectors, Sequences etc...
"""

from BehaviourTree.Node import Node

class Composite(Node):
    def __init__(self):
        Node.__init__(self)
        self. children = []

    def add_node(self, node):
        self.children.append(node)

    def remove_node(self, node):
        self.children.remove(node)


