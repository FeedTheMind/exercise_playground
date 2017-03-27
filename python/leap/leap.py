def is_leap_year(year=1900):
    '''Determines if year is a leap year

    Args: 
        year: numerical value; default = 1900
    Returns: 
        True or False, depending on results of modulo operator 
    '''
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

for year in range(2010, 2021):
    print('{} a leap year . . . '.format(year), is_leap_year(year))
