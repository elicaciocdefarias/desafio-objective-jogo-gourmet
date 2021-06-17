from handlers import HandleFinalizeOrContinue, HandleCreateNodeOrContinue


def title(message):
    print(
        f"""
            {message}
                ***
        """
    )


def loop(node):
    response = input(f"O prato que você pensou é {node}? ")
    if response == "sim":
        finalize_or_continue = HandleFinalizeOrContinue()
        finalize_or_continue.handle(node, loop)
    else:
        create_node_or_continue = HandleCreateNodeOrContinue()
        create_node_or_continue.handle(node, loop)
    return
