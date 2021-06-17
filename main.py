from node import FactoryNode
import game


class Main:
    print(
        """     
            Jogo Gourmet     
                ***
        """
    )
    parent = FactoryNode.factory("massa", "Lasanha", "Bolo de Chocolate")

    while True:
        response = input("Pense em um prato que gosta e digite ok. ")
        if response == "ok":
            game.execute(parent)
        else:
            break


if __name__ == "__main__":
    Main()
