from node import Node, TypeNode
import game


class Main:
    print(
        """     
            Jogo Gourmet     
                ***
        """
    )

    middle = Node("massa", None)
    left = Node("Lasanha", TypeNode.LEFT)
    right = Node("Bolo de Chocolate", TypeNode.RIGHT)

    middle.left = left
    middle.right = right
    left.parent = middle
    right.parent = middle

    while True:
        response = input("Pense em um prato que gosta e digite ok. ")
        if response == "ok":
            game.execute(middle)
        else:
            break


if __name__ == "__main__":
    Main()
