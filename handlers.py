from abc import ABC, abstractmethod

from node import Node, TypeNode


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        ...

    @abstractmethod
    def handle(self, *args):
        ...


class AbstractHandler(Handler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, *args):
        if self._next_handler:
            return self._next_handler.handle(*args)
        return None


class HandleNodeTypeNone(AbstractHandler):
    def handle(self, node, loop):
        if node.type is None:
            return loop(node.right)
        return super().handle(node, loop)


class HandleNodeSideNone(AbstractHandler):
    def handle(self, node, loop):
        side_node = getattr(node, node.type.value)
        if side_node is not None:
            return loop(side_node)
        return super().handle(node)


class HandleUserInputDishName(AbstractHandler):
    def handle(self, node):
        dish_name = input("Qual prato você pensou? ")
        return super().handle(node, dish_name)


class HandleMiddleNode(AbstractHandler):
    def handle(self, node, dish_name):
        left = TypeNode.LEFT
        right = TypeNode.RIGHT
        down_type = left if node.type == right else right
        middle = Node(
            dish_name,
            down_type,
        )
        return super().handle(node.type, node, middle)


class HandleUserInputDishType(AbstractHandler):
    def handle(self, down_type, node, middle):
        dish_type = input(f"{middle} é _______ mas {node} não. ")
        return super().handle(dish_type, down_type, node, middle)


class HandleDownNode(AbstractHandler):
    def handle(self, dish_name, down_type, node, middle):
        down = Node(
            dish_name,
            down_type,
        )
        return super().handle(node, middle, down)


class HandleMiddleSides(AbstractHandler):
    def handle(self, node, middle, down):

        down.parent = node.parent

        down.left = middle if node.type == TypeNode.RIGHT else node
        down.right = node if node.type == TypeNode.RIGHT else middle

        return super().handle(node, middle, down)


class HandleNodeSides(AbstractHandler):
    def handle(self, node, middle, down):
        setattr(node.parent, node.type.value, down)
        node.parent = down
        return super().handle(node, middle, down)


class HandleDownSides(AbstractHandler):
    def handle(self, node, middle, down):
        middle.parent = down
        setattr(down, node.type.value, node)
        return super().handle(node, middle, down)


class HandleFinalizeOrContinue(AbstractHandler):
    def handle(self, node, loop):
        if node.left is None:
            print("Acertei de novo!")
            return super().handle(node, loop)
        return loop(node.left)


class HandleCreateNodeOrContinue:
    def __init__(self):
        self.node_type_none = HandleNodeTypeNone()

    def order_handlers(self):
        handlers = [
            HandleNodeSideNone(),
            HandleUserInputDishName(),
            HandleMiddleNode(),
            HandleUserInputDishType(),
            HandleDownNode(),
            HandleMiddleSides(),
            HandleNodeSides(),
            HandleDownSides(),
        ]

        last = None
        for handle in handlers:
            if self.node_type_none._next_handler is None:
                self.node_type_none.set_next(handle)
            else:
                last.set_next(handle)
            last = handle

    def handle(self, node, loop):
        self.order_handlers()
        return self.node_type_none.handle(node, loop)
