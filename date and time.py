import datetime

# date
d=datetime.date(2023,6,23)
d_today=datetime.date.today()

# datetime
t=datetime.time(23,59,59)
dt=datetime.datetime(2023,6,23,23,59,59)
dt_now=datetime.datetime.now()

# delta time for shifting datetime
delta=datetime.timedelta(days=6)

# format of datetime
string_from_dt=datetime.datetime.strftime(dt_now,"%Y-%d-%m %H:%M:%S")
dt_from_string=datetime.datetime.strptime(string_from_dt,"%Y-%d-%m %H:%M:%S")

if __name__=='__main__':
    print(d)
    print(d_today)

    print(t)
    print(dt)
    print(dt_now)

    print(dt_now+delta)
    print(dt_now-delta)

    print(string_from_dt)
    print(dt_from_string)
