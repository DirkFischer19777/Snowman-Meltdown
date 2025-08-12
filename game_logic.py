import random
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]



def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(ascii_art.STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")
    return display_word

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line


    while True:
        # For now, simply prompt the user once:
        word_status= display_game_state(mistakes, secret_word, guessed_letters)
        compare_lst = word_status.split()
        compare_wrd = "".join(compare_lst)

        if compare_wrd == secret_word:
            print("you solved the word and saved the snowman" )
            return

        # Input validation
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                break
            print("Invalid input. Please enter a single letter (A-Z).")

        print("You guessed:", guess)
        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes +=1
            print(f"wrong guesses: {mistakes}")
            if mistakes > len(ascii_art.STAGES) - 1:
                print("you have failed")
                return

