from node import MiddleNode, Node, TypeNode


def test_middle_node_should_return_node_right_type(monkeypatch):
    monkeypatch.setattr(
        "lists.node.MiddleNode.fromtype",
        lambda _: Node("", TypeNode.RIGHT),
    )

    node = MiddleNode.fromtype(TypeNode.RIGHT)
    assert node.type == TypeNode.RIGHT


def test_middle_node_should_return_node_left_type(monkeypatch):
    monkeypatch.setattr(
        "lists.node.MiddleNode.fromtype",
        lambda _: Node("", TypeNode.LEFT),
    )

    node = MiddleNode.fromtype(TypeNode.LEFT)
    assert node.type == TypeNode.LEFT


def test_should_return_node_with_value_massa(monkeypatch):
    monkeypatch.setattr(
        "lists.node.MiddleNode.fromtype",
        lambda _: Node("massa", TypeNode.RIGHT),
    )

    node = MiddleNode.fromtype(TypeNode.RIGHT)
    assert node.value == "massa"
