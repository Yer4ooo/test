s = 'hello'

i = s.__iter__()

for x in range(0, 5):
    print(next(i).title())
