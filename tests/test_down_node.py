import pytest

from node import DownNode, Node, TypeNode


@pytest.fixture
def fake_node():
    return Node("", None)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (TypeNode.RIGHT, TypeNode.RIGHT),
        (TypeNode.LEFT, TypeNode.LEFT),
    ],
)
def test_down_node_should_return_node_right_type(
    monkeypatch, fake_node, test_input, expected
):
    def mock_fromtype(*args):
        return Node("", test_input)

    monkeypatch.setattr(
        "lists.node.DownNode.fromtype",
        mock_fromtype,
    )

    node = DownNode.fromtype(test_input, fake_node, fake_node)
    assert node.type == expected


def test_should_return_node_with_value_massa(monkeypatch, fake_node):
    def mock_fromtype(*args):
        return Node("massa", TypeNode.LEFT)

    monkeypatch.setattr(
        "lists.node.DownNode.fromtype",
        mock_fromtype,
    )

    node = DownNode.fromtype(TypeNode.LEFT, fake_node, fake_node)
    assert node.value == "massa"
