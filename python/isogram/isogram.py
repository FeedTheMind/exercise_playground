def is_isogram(word):
    '''Checks to see if word is an isogram,
    a word that doesn't repeat any letters

    Args: 
        word = string 
    Returns:
        True or False
    '''
    lower = word.lower()
    for a in {b:lower.count(b) for b in lower if b.isalpha()}.values():
        if a > 1:
            return False

    return True

words = [
    'hello',
    'what',
    'goodbye',
    'bold',
    'courageous',
    'Daring',
    'Alphabet',
    'Time',
    'newspaper'
]

for word in words:
    print('{} an isogram . . . '.format(word), is_isogram(word))
