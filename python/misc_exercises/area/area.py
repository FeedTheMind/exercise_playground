values = [
    (4, 8),
    (5, 10),
    (6, 12),
    (7, 14),
    (10, 10)
]

def area(arg):
    '''Multiples first item by second item

    Arguments:
        arg = tuple of two values . . . Ex: (1, 2)
    Returns:
        Value of first item * second item
    '''
    return arg[0] * arg[1]


areas = [area(i) for i in values]

print('%s . . . ' % (values), areas)
