from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    return [word.strip() for word in open(DICTIONARY, 'r').readlines()]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES.get(letter.upper(),0) for letter in word])

def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    word_list = load_words() if word_list is None else word_list
    word_score = {word:calc_word_value(word) for word in word_list}
    return max(word_score, key= lambda k: word_score[k])

if __name__ == "__main__":
    pass