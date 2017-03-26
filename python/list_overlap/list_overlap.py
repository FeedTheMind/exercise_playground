import random

def remove_and_sort(size=100, length=20):
    '''Removes duplicates and sorts values

    Args: 
        size: the size of the range; default = 100
        length = returns list of unique elements; default = 20
    Returns:
        sorted list of numbers
    '''
    a = random.sample(range(size), length)
    # Adds 5 to length of b to compare against different list sizes
    b = random.sample(range(size), length + 5)
    print(a)
    print(b)

    return sorted(list(set([num for num in a if num in b])))

print('Sorted list of numbers, without duplicates: ',remove_and_sort())
