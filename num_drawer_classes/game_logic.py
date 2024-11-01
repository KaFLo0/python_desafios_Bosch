from . import number_drawer as numdrw
from . import player


class GameLogic(numdrw.NumberDrawer):
    def __init__(self) -> None:
        super().__init__()
        self.drawer: numdrw.NumberDrawer = numdrw.NumberDrawer()
        self.player: player.Player = player.Player()

    def verify_guess(self, guess: int) -> str:
        if guess == self.drawer.get_number_drawed():
            return "Congratulations, you guessed right!\n"
        self.calculate_diff(guess)
        if self.player.get_lifes() <= 0 or self.player.get_chances() == 0:  # Game Over condition
            return f"****GAME OVER****\nThe Number drawed was: {self.drawer.get_number_drawed()}"
        elif self.player.get_lifes() <= 25 or self.player.get_chances() == 1:  # Here I checking if the player has less
            #  equal than 25 lifes or exactly 1 chance, I used "or" to especifically treat both conditions appart
            #  in the if's statement below, this helps the player to stay up on his stats
            if self.player.get_lifes() <= 25 and self.player.get_chances() >= 1:
                return (f"You running out of lifes! You have only {self.player.get_lifes()} lifes. "
                        f"Oh, and you still have {self.player.get_chances()} chances.")
            elif self.player.get_lifes() > 25 and self.player.get_chances() == 1:
                return (f"You are running out fo chances! You have only {self.player.get_chances()} chances. "
                        f"Oh, but you still have {self.player.get_lifes()} lifes.")
            return (f"OMG, You are low both on lifes AND chances! Your stats are {self.player.get_lifes()} lifes and "
                    f"{self.player.get_chances()} chances...\nI wish you good luck!")
        else:
            return (f"You guessed wrong, but don't worry, you still have {self.player.get_lifes()} lifes and "
                    f"{self.player.get_chances()} chances.")

    def calculate_diff(self, guess: int) -> None:
        diff: int = abs(self.drawer.get_number_drawed() - guess)
        return self.decrement_lifes_chances(diff)

    def decrement_lifes_chances(self, diff: int) -> None:
        self.player.set_lifes((self.player.get_lifes() - diff))
        self.player.set_chances((self.player.get_chances() - 1))
