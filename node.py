from typing import Union
from enum import Enum


class TypeNode(Enum):
    LEFT = "left"
    RIGHT = "right"


class Node:
    def __init__(self, value, type):
        self.value = value
        self.parent: Union[Node, None] = None
        self.left: Union[Node, None] = None
        self.right: Union[Node, None] = None
        self.type: Union[TypeNode, None] = type

    def __str__(self):
        return self.value


class MiddleNode:
    @classmethod
    def fromtype(cls, type):
        message = "Qual prato você pensou? "
        node = Node(
            input(message),
            type,
        )
        return node


class DownNode:
    @classmethod
    def fromtype(cls, type, node, middle):
        message = f"{middle} é _______ mas {node} não. "
        node = Node(
            input(message),
            type,
        )
        return node


class DefineSidesNodes:
    def __init__(self, node, middle, down):
        self.node = node
        self.middle = middle
        self.down = down

    def define_middle_sides(self):
        self.middle.parent = self.node.parent
        self.middle.left = self.down if self.node.type == TypeNode.RIGHT else self.node
        self.middle.right = self.node if self.node.type == TypeNode.RIGHT else self.down

    def define_node_sides(self):
        side = "right" if self.node.type == TypeNode.RIGHT else "left"
        setattr(self.node.parent, side, self.middle)
        self.node.parent = self.middle

    def define_down_sides(self):
        side = "right" if self.node.type == TypeNode.RIGHT else "left"
        self.down.parent = self.middle
        setattr(self.down, side, self.node)

    @classmethod
    def to(cls, node, middle, down):
        instance = cls(node, middle, down)
        instance.define_middle_sides()
        instance.define_node_sides()
        instance.define_down_sides()
