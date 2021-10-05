from datetime import datetime as dt

delta = dt.now() - dt(year=1993, month=3, day=11)
print(delta)
print(delta.month)
