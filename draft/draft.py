from typing import List, Tuple

def get_word() -> str:
    """
    Prompt the chooser player for his word and return that word.

    Returns:
        str
    """
    while True:
        word = input("Please choose a word: ")
        if word.isalpha():
            break
    return word.lower()


def get_lives() -> int:
    """
    Prompt the chooser player for a number of lives and return this number of lives.

    Returns:
        int
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
    Prompt the guesser player to suggest a letter.

    Returns:
        str
    """
    while True:
        letter = input("Guess a letter of the secret word: ")
        if letter.isalpha() and len(letter) == 1:
            break
    return letter.lower()


def access_guess(secret_word:str, guessed_letter:str, lives_left:int) -> Tuple[bool, int]:
    """
    Take as arguments: 'secret_word', the word to be guessed;
    'guessed_letter', the last letter suggested from guesser player;
    'lives_left', the number of lives left.

    Output if the guess is correct or not,
    and return the current number of lives of the player, depending on the outcome of the guess.

    Args:
        str: The secret word to guess.
        str: The guessed letter.
        int: The number of lives left.
    
    Returns:
        Tuple[bool, int]: A list of two elements, where first element is a boolean
        and the second an integer.
    """
    correct = guessed_letter in secret_word
    if not correct:
        lives_left -= 1
    return correct, lives_left


def display_word(secret_word:int, suggested_letters:List[str]) -> Tuple[str, bool]:
    """
    Take as arguments: 'secret_word', the word to be guessed;
    'suggested_letters', a list of the letters suggested by 
    the guesser player throughout the game.

    Display the secret word with white spaces between the letters,
    hiding the non-guessed letters by replacing them with '_';
    and return True if the correct word has been found, False otherwise.

    Args:
        int: The secret word.
        List[str]: The list of the suggested letters.
    
    Returns:
        Tuple[str, bool]: A list of two elements, where first element is a string
        and the second a boolean.
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
        return " ".join(guessed_list), False
    else:
        return " ".join(guessed_list), True


def main():
    """
    Orchestrate a full hangman game.
    """
    secret_word = get_word()
    lives_left = get_lives()
    suggested_letters = []

    while lives_left > 0:
        guessed_letter = get_guess()
        suggested_letters.append(guessed_letter)
        correct, lives_left = access_guess(secret_word, guessed_letter, lives_left)
        print(f"Your guess was '{correct}' and you have {lives_left} lives left.")
        guessed_word, found = display_word(secret_word, suggested_letters)
        print(guessed_word)
        if found:
            print(f"You found the secret word: '{secret_word}'. Bravo!")
            break
    if lives_left == 0 and not found:
        print(f"Game over! Sorry, you loose. You guessed '{guessed_word}', but the secret word was '{secret_word}'")

main()