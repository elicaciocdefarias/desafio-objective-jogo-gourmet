from node import DefineSidesNodes, DownNode, MiddleNode, TypeNode


def execute(node):
    response = input(f"O prato que você pensou é {node}? ")
    if response == "sim":
        finalize_or_continue = FinalizeOrContinue(node, execute)
        finalize_or_continue.execute()
    else:
        create_node_or_continue = CreateNodeOrContinue(
            node,
            execute,
            MiddleNode,
            DownNode,
            DefineSidesNodes,
        )
        create_node_or_continue.execute()
    return


class FinalizeOrContinue:
    def __init__(self, node, function_execute):
        self.node = node
        self.function_execute = function_execute

    def execute(self):
        if self.node.left is None:
            print("Acertei de novo!")
            return
        return self.function_execute(self.node.left)


class CreateNodeOrContinue:
    def __init__(
        self,
        node,
        loop,
        middle_node,
        down_node,
        define_sides_nodes,
    ):
        self.node = node
        self.loop = loop
        self.middle_node = middle_node
        self.down_node = down_node
        self.define_sides_nodes = define_sides_nodes

    def define(self):
        down_type = (
            TypeNode.LEFT if self.node.type == TypeNode.RIGHT else TypeNode.RIGHT
        )
        middle = self.middle_node.fromtype(self.node.type)
        down = self.down_node.fromtype(down_type, self.node, middle)
        self.define_sides_nodes.to(self.node, middle, down)

    def execute(self):
        if self.node.type is None:
            return self.loop(self.node.right)

        side_node = getattr(self.node, self.node.type.value)
        if side_node is not None:
            return self.loop(side_node)
        return self.define()
