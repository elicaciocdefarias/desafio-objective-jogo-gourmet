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
            node.type,
        )
        return super().handle(down_type, node, middle)


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
        middle.parent = node.parent
        middle.left = down if node.type == TypeNode.RIGHT else node
        middle.right = node if node.type == TypeNode.RIGHT else down
        return super().handle(node, middle, down)


class HandleNodeSides(AbstractHandler):
    def handle(self, node, middle, down):
        side = "right" if node.type == TypeNode.RIGHT else "left"
        setattr(node.parent, side, middle)
        node.parent = middle
        return super().handle(node, middle, down)


class HandleDownSides(AbstractHandler):
    def handle(self, node, middle, down):
        side = "right" if node.type == TypeNode.RIGHT else "left"
        down.parent = middle
        setattr(down, side, node)
        return super().handle(node, middle, down)


class HandleFinalizeOrContinue(AbstractHandler):
    def handle(self, node, loop):
        if node.left is None:
            print("Acertei de novo!")
            return super().handle(node, loop)
        return loop(node.left)
