class Player:
    def __init__(self) -> None:
        self.__lifes: int = 100
        self.__chances: int = 5

    def calculate_diff(self, guess: int) -> None:
        pass

    def decrement_lifes_chances(self, diff: int) -> None:
        pass

    def get_lifes(self) -> int:
        return self.__lifes

    def get_chances(self) -> int:
        return self.__chances

    def set_lifes(self, value: int) -> None:
        self.__lifes = value

    def set_chances(self, value: int) -> None:
        self.__chances = value
