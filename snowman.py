import game_logic





def repeat_game():
    while True:
        game_logic.play_game()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break



if __name__ == "__main__":
    repeat_game()
