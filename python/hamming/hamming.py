def difference(first, second):
    '''Raise ValueError if first and second do not match

    Arguments:
        first = string
        second = string
    Returns:
        Either ValueError or None
    '''
    if len(first) != len(second):
        raise ValueError('Both strings must be of equal length.')
    return None

def distance(DNA, comparison):
    '''Checks first element of first parameter with 
    first element of second parameter, increasing count if different

    Arguments:
        DNA = string
        comparison = string
    Returns:
        Count difference or ValueError if unequal lengths
    '''
    count = 0

    difference(DNA, comparison)

    for i, x in zip(DNA, comparison):
        if i != x:
            count += 1
    return count
