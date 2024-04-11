import datetime as dt
bday = dt.datetime(2000, 10, 14, hour=12, minute=0)
dt_now = dt.datetime.now()
alive = dt_now - bday
secs = (alive.days * 24 * 60 * 60) + alive.seconds
res = f"I have been alive for {secs:,.0f} secs"
print(res)

days = 1340
future = dt.datetime.now() + dt.timedelta(days=days)
alive = future - bday
age = alive.days/365.
res = f"In {days} days, I'll be {age:.2f} years old"
print(res)