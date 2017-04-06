from datetime import datetime as DT

dates = [
    DT(2012, 12, 15),
    DT(1987, 8, 20),
    DT(1965, 2, 28),
    DT(2012, 6, 27)
]

def is_2012(arg):
    return arg.year == 2012

dt_2012 = filter(is_2012, dates)

print(next(dt_2012))
print(next(dt_2012))
