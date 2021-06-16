import pytest
from node import Node, DefineSidesNodes, TypeNode


@pytest.fixture
def define_sides_right():
    parent = Node("", TypeNode.RIGHT)
    node = Node("", TypeNode.RIGHT)
    node.parent = parent
    middle = Node("", TypeNode.RIGHT)
    down = Node("", TypeNode.LEFT)
    return DefineSidesNodes(node, middle, down)


@pytest.mark.parametrize(
    "side, type", [("right", TypeNode.RIGHT), ("left", TypeNode.LEFT)]
)
def test_should_return_middle_side_correct(define_sides_right, side, type):
    define_sides_right.define_middle_sides()
    side_node = getattr(define_sides_right.middle, side)
    assert side_node.type == type


def test_should_have_parent_node_not_equal_none(define_sides_right):
    define_sides_right.define_middle_sides()
    assert define_sides_right.middle.parent is not None


def test_should_define_node_parent_correct(define_sides_right):
    define_sides_right.define_node_sides()
    assert define_sides_right.node.parent == define_sides_right.middle


def test_should_define_down_parent_correct(define_sides_right):
    define_sides_right.define_down_sides()
    assert define_sides_right.down.parent == define_sides_right.middle
