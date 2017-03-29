def is_pangram(string):
    '''Determines if string has every letter
    of the alphabet

    Args: 
        string = phrase
    Returns: 
        True or False
    '''
    ABCs = 'abcdefghijklmnopqrstuvwxyz'
    lower = string.lower()

    return all(letter in lower for letter in ABCs)
    
print('A pangram has every letter of the alphabet.')

print('\nPangram: The quick brown fox jumps over the lazy dog . . . ', is_pangram('The quick brown fox jumps over the lazy dog'))

print('\nPangram: This sentence has every letter of the alphabet . . . ', is_pangram('This sentence has every letter of the alphabet'))
