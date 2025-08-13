import game_logic # Import the game logic module


def repeat_game():
    """
        Run the game in a loop, asking the player
        if they want to play again after each round.
    """
    while True:
        game_logic.play_game() # Start a new game

        # Ask the player if they want to play again
        again = input("Do you want to play again? (y/n): ").lower()

        # Exit loop if answer is not 'y'
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    repeat_game()
