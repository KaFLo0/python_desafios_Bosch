import random
from . import player


class NumberDrawer(player.Player):
    def __init__(self) -> None:
        super().__init__()
        self._number_drawed: int = random.randint(1, 100)
        self.player = player.Player()

    def get_number_drawed(self) -> int:
        return self._number_drawed

    def __set_number_drawed(self, value: int) -> None:
        self._number_drawed = value
