records = [('foo', 1, 2),
           ('bar', 'madhu'),
           ('foo', 3, 8)]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(name):
    print('bar', name)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

