from typing import List
from random import choice

class Hangman:
    """
    This class has seven attributes.

    :'possible_words' contains a list of words. Out of these words, one will be selected as the word to find.
    The list must also contain the following words: 'becode', 'learning', 'mathematics', 'sessions'.

    :'word_to_find' contains a list of strings, whose elements are the letter of the word to guess.

    :'lives' is the number of lives that the player still has left. It starts at 5.

    :'correctly_guessed_letters' contains a list of strings where each element will be a letter guessed by the user.

    :'wrongly_guessed_letters' contains a list of strings where each element will be a letter guessed
    by the user that is not in the 'word_to_find'.

    : 'turn_count' contains the number of turns played by the player. It is represented as an int.

    : 'error_count' contains the number of errors made by the player.

    This class provides four methods.

    : 'play()' method.

    : 'start_game()' method.

    : 'game_over()' method.

    : 'well played()' method.
    """

    def __init__(self, lives: int = 5, possible_words:List[str] = []):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        for word in possible_words:
            self.possible_words.append(word)
        self.word_to_find = [letter for letter in choice(self.possible_words)]

        if len(set(self.word_to_find)) <= lives:
            self.lives = lives
        else:
            self.lives = len(set(self.word_to_find))
        
        self.correctly_guessed_letters = ['_' for letter in self.word_to_find]
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0


    def play(self):
        """
        This method asks the player to enter a letter.
        """
        while True:
            letter = input("Guess a letter of the secret word: ")
            if letter.isalpha() and len(letter) == 1:
                break
        if letter in self.word_to_find:
            indexes = (i for i in range(len(self.word_to_find)) if self.word_to_find[i] == letter)
            for index in indexes:
                self.correctly_guessed_letters[index] = letter
        else:
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1
            self.lives -= 1
        self.turn_count += 1
        return letter.lower()


    def start_game(self):
        """
         This method calls the play() method until the game is over.
        """
        while self.lives > 0:
            self.play()
            print(f"This was turn number {self.turn_count}.")
            print(f"The correctly guessed letters are: {' '.join(self.correctly_guessed_letters)}.")
            print(f"The bad guessed letters are: {', '.join(self.wrongly_guessed_letters)}.")
            print(f"You have {self.lives} turns left, and have done {self.error_count} errors.")
            print("*********************************************************")
            if self.correctly_guessed_letters == self.word_to_find:
                print(self.well_played())
                break
        if self.lives == 0 and self.correctly_guessed_letters != self.word_to_find:
            print(self.game_over())


    def game_over(self):
        return "Sorry, you loose! Game over ..."

    def well_played(self):
        return f"Bravo! You found the word, '{''.join(self.word_to_find)}', in {self.turn_count} turns with {self.error_count} errors!"