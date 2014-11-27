first = ['bucky', 'tom', 'taylor']
last = ['roberts', 'hanks', 'swift']

names = zip (first, last)
# it will make something like [('bucky','roberts'),('tom','hanks'),('taylor','swift')]
for a, b in names:
    print(a,b)