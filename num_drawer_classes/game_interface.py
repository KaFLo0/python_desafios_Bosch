from . import game_logic as gl


class GameInterface(gl.GameLogic):
    def __init__(self) -> None:
        super().__init__()
        self.game: None = None

    def start_game(self) -> None:
        self.game = gl.GameLogic()
        print("Welcome to 'Guess tem number' game! Are you with good lucky today? Play the game now and find out!")

    def play_game(self) -> bool:
        while self.game.player.get_lifes() > 0 and self.game.player.get_chances() > 0:
            try:

                user_guess: int = int(input("Guess a number between 1 and 100: "))
                if not 1 <= user_guess <= 100:
                    print("Please enter only a number between 1 and 100.")
                    continue
                result: str = self.game.verify_guess(user_guess)
                print(result)
                if "Congratulations" in result:
                    return self.ask_player_toplay_again()

            except ValueError:
                print("Please, enter with a valid number.")
        return self.ask_player_toplay_again()

    def run(self) -> None:
        while True:
            self.start_game()
            play_again = self.play_game()
            if not play_again:
                print("Thank you for playing! I 'guess' you had a good time playing hahaha.")
                break

    @staticmethod
    def ask_player_toplay_again() -> bool:
        user_choice = input("Do you want to start a new game?(Y/n): ")
        return user_choice == 'Y'
