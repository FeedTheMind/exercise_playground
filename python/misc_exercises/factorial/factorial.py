def factorial(n):
    '''Returns the factorial of a number (n)

    Arguments:
        n = number
    Returns:
        Factorial of n
    '''
    if n == 1:
        return 1
    return n * factorial(n-1)

for i in range(1, 11):
    print('The factorial of {} is . . . '.format(i), factorial(i))
