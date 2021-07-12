import datetime

name = 'Andrew'
hoy = datetime.datetime.today()
mañana = hoy + datetime.timedelta(days=1)

print(f"Hello, world. My name is {name}.")
print(f"Today is {hoy: %B %d, %Y} and tomorrow is {mañana: %B %d, %Y}.")
print("The future doesn't exist. There is only now.")
