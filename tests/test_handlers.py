from handlers import (
    HandleNodeTypeNone,
    HandleNodeSideNone,
    HandleUserInputDishName,
    HandleMiddleNode,
    HandleUserInputDishType,
    HandleDownNode,
    HandleMiddleSides,
    HandleNodeSides,
    HandleDownSides,
    HandleFinalizeOrContinue,
    HandleCreateNodeOrContinue,
)
from node import Node, TypeNode


def test_handle_node_type_none_sides_should_called_once_with_correct_arguments(mocker):
    node = Node("", None)

    def fake_loop(node):
        return

    node_type_node = HandleNodeTypeNone()
    spy = mocker.spy(node_type_node, "handle")

    node_type_node.handle(node, fake_loop)
    spy.assert_called_once_with(node, fake_loop)


def test_handle_node_side_none_sides_should_called_once_with_correct_arguments(mocker):
    node = Node("", TypeNode.RIGHT)

    def fake_loop(node):
        return

    node_side_none = HandleNodeSideNone()
    spy = mocker.spy(node_side_none, "handle")

    node_side_none.handle(node, fake_loop)
    spy.assert_called_once_with(node, fake_loop)


def test_handle_user_input_dish_name_should_called_once_with_correct_arguments(mocker):
    def fake_handle(*args):
        return args

    mocker.patch(
        "handlers.HandleUserInputDishName.handle",
        fake_handle,
    )
    node = Node("", None)
    user_input_dish_name = HandleUserInputDishName()
    spy = mocker.spy(user_input_dish_name, "handle")

    user_input_dish_name.handle(node)
    spy.assert_called_once_with(node)


# def test_handle_user_input_dish_name_should_correct_text(mocker):
#     def fake_handle(*args):
#         return args

#     mocker.patch(
#         "handlers.HandleUserInputDishName.handle",
#         fake_handle,
#     )
#     node = Node("", None)
#     user_input_dish_name = HandleUserInputDishName()
#     result = user_input_dish_name.handle(node)
#     print(result)
#     assert result is None


def test_handle_middle_node_should_called_once_with_correct_arguments(mocker):
    node = Node("", None)
    dish_name = "massa"
    middle_node = HandleMiddleNode()
    spy = mocker.spy(middle_node, "handle")

    middle_node.handle(node, dish_name)
    spy.assert_called_once_with(node, dish_name)


def test_handle_user_input_dish_type_should_called_once_with_correct_arguments(mocker):
    def fake_handle(*args):
        return args

    mocker.patch(
        "handlers.HandleUserInputDishType.handle",
        fake_handle,
    )

    node = Node("", None)
    middle = node
    down_type = TypeNode.RIGHT
    user_input_dish_type = HandleUserInputDishType()
    spy = mocker.spy(user_input_dish_type, "handle")

    user_input_dish_type.handle(down_type, node, middle)
    spy.assert_called_once_with(down_type, node, middle)


def test_handle_down_node_should_called_once_with_correct_arguments(mocker):
    node = Node("", None)
    middle = node
    dish_name = "massa"
    down_type = TypeNode.RIGHT
    down_node = HandleDownNode()
    spy = mocker.spy(down_node, "handle")

    down_node.handle(dish_name, down_type, node, middle)
    spy.assert_called_once_with(dish_name, down_type, node, middle)


def test_handle_middle_sides_should_called_once_with_correct_arguments(mocker):
    node = Node("", None)
    middle = node
    down = node

    middle_sides = HandleMiddleSides()
    spy = mocker.spy(middle_sides, "handle")

    middle_sides.handle(node, middle, down)
    spy.assert_called_once_with(node, middle, down)


def test_handle_node_sides_should_called_once_with_correct_arguments(mocker):
    parent = Node("", None)
    node = Node("", TypeNode.RIGHT)
    node.parent = parent
    middle = node
    down = node

    node_sides = HandleNodeSides()
    spy = mocker.spy(node_sides, "handle")

    node_sides.handle(node, middle, down)
    spy.assert_called_once_with(node, middle, down)


def test_handle_down_sides_should_called_once_with_correct_arguments(mocker):
    node = Node("", TypeNode.RIGHT)
    middle = node
    down = node

    down_sides = HandleDownSides()
    spy = mocker.spy(down_sides, "handle")

    down_sides.handle(node, middle, down)
    spy.assert_called_once_with(node, middle, down)


def test_handle_finalize_sides_should_called_once_with_correct_arguments(mocker):
    node = Node("", None)

    def fake_loop(node):
        return

    finalize_or_continue = HandleFinalizeOrContinue()
    spy = mocker.spy(finalize_or_continue, "handle")

    finalize_or_continue.handle(node, fake_loop)
    spy.assert_called_once_with(node, fake_loop)


def test_handle_create_node_or_continue_should_called_once_with_correct_arguments(
    mocker,
):
    node = Node("", None)

    def fake_loop(node):
        return

    create_node_or_continue = HandleCreateNodeOrContinue()
    spy = mocker.spy(create_node_or_continue, "handle")

    create_node_or_continue.handle(node, fake_loop)
    spy.assert_called_once_with(node, fake_loop)
