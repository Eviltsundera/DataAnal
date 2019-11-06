from collections.abc import Iterable
def product(a):
    if len(a) == 2:
        for x in a[0]:
            for y in a[1]:
                if isinstance(x, Iterable):
                    yield (*x, y)
                else:
                    yield (x, y)
    else:
        b = a
        if isinstance(b[0][0], Iterable):
            b[0] = ([(*x, y) for x in a[0] for y in a[1]])
        else:
            b[0] = ([(x, y) for x in a[0] for y in a[1]])
        #b[0] = ([(x, y) for x in a[0] for y in a[1]])
        del b[1]
        yield from product(b)


#a = [[1, 2], [3, 4], [5, 6], [7, 8]]

#for e in product(a):
 #   print(e)



