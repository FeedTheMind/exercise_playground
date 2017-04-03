from datetime import timedelta as TD

def add_gigasecond(birth):
    '''Returns when a person has lived for
    10**9 seconds

    Arguments:
        birth = datetime(year, month, day)
    Returns: 
        Moment person has live for 10**9 seconds
    '''
    time_delta = TD(seconds = 10**9)
    birth = birth

    return (time_delta + birth)
