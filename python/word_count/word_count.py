import re

def word_count(sentence):
    '''Returns dictionary with number 
    of times word appears in sentence

    Args:
        sentence = string
    Returns: 
        dictionary with count
    '''

    words = [word for word in re.split('[_\W]', sentence.lower()) if word.isalnum()]

    return {word:words.count(word) for word in words}

print(word_count('hey,my_spacebar_is_broken.'))
