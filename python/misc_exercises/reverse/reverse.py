def reverse(iterable):
    '''Returns reversed version
    of single iterable item

    Arguments:
        iterable = iterable item
    Returns:
        Reversed form
    '''
    return iterable[::-1]

print(reverse('!olleH'))
print(reverse('!eybdooG'))


forwards = map(reverse, ['!eybdooG ,!olleH'])

print(list(forwards))
