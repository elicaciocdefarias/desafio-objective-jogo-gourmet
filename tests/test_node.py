import pytest
from node import FactoryNode, Node


@pytest.fixture
def node():
    return FactoryNode.factory("massa", "Lasanha", "Bolo de Chocolate")


def test_should_return_node(node):
    assert isinstance(node, Node)


def test_should_return_node_with_right_side_not_equal_node(node):
    assert node.right is not None


def test_should_return_node_with_left_side_not_equal_node(node):
    assert node.left is not None
