import itertools
import unittest

from game import draw_letters, calc_word_value, max_word_value
from game import WordsGenerator
from game import _validation

NUM_LETTERS = 7
TEST_WORDS = ('bob', 'julian', 'pybites', 'quit', 'barbeque')

class TestGame(unittest.TestCase):

    def setUp(self):
        self.draw = draw_letters()

    def test_draw_letters(self):
        letter_str = ''.join(self.draw)
        self.assertRegex(letter_str, r'^[A-Z]{%s}$' % NUM_LETTERS)

    # from ch01
    def test_calc_word_value(self):
        self.assertEqual(calc_word_value('bob'), 7)
        self.assertEqual(calc_word_value('JuliaN'), 13)

    # from ch01
    def test_max_word_value(self):
        self.assertEqual(max_word_value(TEST_WORDS), 'barbeque')

    def test_WordGenerator(self):
        # test WordGenerator._get_permutations_draw()
        word_gen = WordsGenerator(self.draw)
        gen_permutations_n_letters = sum(len(list(itertools.permutations(self.draw, n))) for n in range(1, NUM_LETTERS+1))
        game_permutations = len(list(word_gen._get_permutations_draw()))
        self.assertEqual(gen_permutations_n_letters, game_permutations)
        alist = range(1,8)
        gen_permutations_any_list = sum(len(list(itertools.permutations(alist, n))) for n in range(1, NUM_LETTERS+1))
        self.assertEqual(gen_permutations_any_list, gen_permutations_n_letters)
        # test WordGenerator.get_possible_dict_words()
        self.fixed_draw = list('garytev'.upper())
        word_gen = WordsGenerator(self.fixed_draw)
        words = word_gen.get_possible_dict_words()
        self.assertEqual(len(words), 137)

    def test_validation(self):      
        draw = list('garytev'.upper())
        word = 'GARYTEV'
        self.assertRaises(ValueError, _validation, word, draw)
        word = 'F'
        self.assertRaises(ValueError, _validation, word, draw)
        word = 'GARETTA'
        self.assertRaises(ValueError, _validation, word, draw)
        try:
            word = 'gary'
            _validation(word, draw)
        except:
            self.fail("_validation() could not handle a valid lower case input")       

if __name__ == "__main__":
   unittest.main() 
