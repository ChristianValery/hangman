from typing import List

def get_word() -> str:
    """
    This function prompts the chooser player for his word and returns that word.
    """
    while True:
        word = input("Please choose a word: ")
        if word.isalpha():
            break
    return word.lower()


def get_lives() -> int:
    """
    This function prompts the chooser player for a number of lives and returns this number of lives.
    """
    while True:
        lives_number = input("Please enter the number of lives (a positive integer): ")
        try:
            int(lives_number)
        except ValueError:
            continue
        if int(lives_number) > 0:
            break
    return int(lives_number)


def get_guess() -> str:
    """
    This function prompts the guesser player to suggest a letter.
    """
    while True:
        letter = input("Guess a letter of the secret word: ")
        if letter.isalpha() and len(letter) == 1:
            break
    return letter.lower()


def assess_guess(secret_word:str, guessed_letter:str, lives_left:int) -> List[bool | int]:
    """
    This function takes as arguments:
    'secret_word', the word to be guessed;
    'guessed_letter', the last letter suggested from guesser player;
    'lives_left', the number of lives left.

    It then outputs if the guess is correct or not,
    and returns the current number of lives of the player,
    depending on the outcome of the guess.
    """
    correct = guessed_letter in secret_word
    lives_left -= 1
    return [correct, lives_left]


def display_word(secret_word:int, suggested_letters:List[str]) -> List[str | bool]:
    """
    This function takes as arguments:
    'secret_word', the word to be guessed;
    'suggested_letters', a list of the letters suggested by 
    the guesser player throughout the game.

    It then displays the secret word with white spaces between the letters,
    hiding the non-guessed letters by replacing them with '_'; and it
    returns True if the correct word has been found, False otherwise.
    """
    word_list = [letter for letter in secret_word]
    guessed_list = ['_' for letter in secret_word]
    for letter in suggested_letters:
        if letter in word_list:
            indexes = (i for i in range(len(word_list)) if word_list[i] == letter)
            for index in indexes:
                guessed_list[index] = letter
                word_list[index] = '_'
    if any(letter == '_' for letter in guessed_list):
        return [" ".join(guessed_list), False]
    else:
        return [" ".join(guessed_list), True]


def main():
    """
    This function orchestrates a full hangman game.
    """
    secret_word = get_word()
    lives_left = get_lives()
    suggested_letters = []

    while lives_left > 0:
        guessed_letter = get_guess()
        suggested_letters.append(guessed_letter)
        correct, lives_left = assess_guess(secret_word, guessed_letter, lives_left)
        print(f"Your guess was '{correct}' and you have {lives_left} lives left.")
        guessed_word, found = display_word(secret_word, suggested_letters)
        print(guessed_word)
        if found:
            print(f"You found the secret word: '{secret_word}'. Bravo!")
            break
    if lives_left == 0 and not found:
        print(f"Game over! Sorry, you loose. You guessed '{guessed_word}', but the secret word was '{secret_word}'")

main()