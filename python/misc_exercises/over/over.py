from datetime import datetime as DT

birthdays = [
    DT(2012, 4, 29),
    DT(2006, 8, 9),
    DT(1978, 5, 16),
    DT(1981, 8, 15),
    DT(2001, 7, 4),
    DT(1999, 12, 30)
]

def is_over_13(dt):
    '''Returns True or False if >= 4745 (days)'''
    today = DT.today()
    return (today - dt).days >= 4745

def date_string(dt):
    '''Returns formatted datetime, as string'''
    return dt.strftime("%B %d")

birth_dates = map(date_string, filter(is_over_13, birthdays))

print(list(birth_dates))
