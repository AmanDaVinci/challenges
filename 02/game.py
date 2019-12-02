#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return random.choices(POUCH, k=NUM_LETTERS)


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    word = input("Form a word: ").lower()
    _validation(word, draw)
    return word


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    # TODO: Optimize this code
    word_from_draw = True
    for letter in word:
        if letter.upper() in draw: draw.remove(letter.upper())
        else:                      word_from_draw = False; break
    if not word_from_draw or word not in DICTIONARY:
        raise ValueError("Invalid Word")

# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).

class WordsGenerator():
    """ Generates all possible dictionary words from a draw of letters
    """
    def __init__(self, draw):
        self.draw = draw

    def _get_permutations_draw(self):
        """Helper for get_possible_dict_words to get all permutations of draw letters.
        Hint: use itertools.permutations"""
        words = []
        for i in range(1,len(self.draw)+1):
            for letters in itertools.permutations(self.draw, i):
                words.append(''.join(letters))
        return words

    def get_possible_dict_words(self):
        """Get all possible words from draw which are valid dictionary words.
        Use the _get_permutations_draw helper and DICTIONARY constant"""
        words = self._get_permutations_draw()
        return [word for word in words if word.lower() in DICTIONARY]

# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    word_gen = WordsGenerator(draw)
    possible_words = word_gen.get_possible_dict_words()

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
