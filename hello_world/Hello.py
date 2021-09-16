"""
This program is meant to be a simple demo to start off my new repository.
"""


def main():
    """
    The main function defined.
    """

    stop = False
    while not stop:

        # find out what to say.
        comment = float(
            input("1. Say 'Hello World!'\n2. Say 'Goodbye World!'\n3. Exit.\n")
        )

        # say what the user wants to be said.
        if comment == 1:
            print("\nHello World!\n")
        elif comment == 2:
            print("\nGoodbye World!\n")
        elif comment == 3:
            stop = True

    # exit message.
    print("\nOkay bye.")


# call the main function.
main()
