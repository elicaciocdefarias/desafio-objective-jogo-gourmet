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
