from handlers import (
    HandleFinalizeOrContinue,
    HandleNodeTypeNone,
    HandleNodeSideNone,
    HandleUserInputDishName,
    HandleMiddleNode,
    HandleUserInputDishType,
    HandleDownNode,
    HandleMiddleSides,
    HandleNodeSides,
    HandleDownSides,
)


def execute(node):
    response = input(f"O prato que você pensou é {node}? ")
    if response == "sim":
        finalize_or_continue = HandleFinalizeOrContinue()
        finalize_or_continue.handle(node, execute)
    else:
        node_type_none = HandleNodeTypeNone()
        node_side_none = HandleNodeSideNone()
        user_input_dish_name = HandleUserInputDishName()
        middle_node = HandleMiddleNode()
        user_input_dish_type = HandleUserInputDishType()
        down_node = HandleDownNode()
        middle_sides = HandleMiddleSides()
        node_sides = HandleNodeSides()
        down_sides = HandleDownSides()

        node_type_none.set_next(node_side_none).set_next(user_input_dish_name).set_next(
            middle_node
        ).set_next(user_input_dish_type).set_next(down_node).set_next(
            middle_sides
        ).set_next(
            node_sides
        ).set_next(
            down_sides
        )
        node_type_none.handle(node, execute)
    return
