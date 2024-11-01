"""
    Sortear um número entre 1 e 100.
    import random | randint() randrange() | Vida = 100 | Chances = 5
    "Qual número foi sorteado?"
    Vars:
        - Sorteado:int = 30
        - Usuário:int = 75
        - Vida Atual:int = 100 - (75 - 30)
        - Vida Atual:int = 100 - 45
        - Vida Atual:int = 55
        - Chances:int = 4
"""
from num_drawer_classes import game_interface


def main() -> None:
    interface = game_interface.GameInterface()
    interface.run()


if __name__ == '__main__':
    main()
