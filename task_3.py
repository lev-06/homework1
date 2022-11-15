 def foo(x,y):
    c = []
    z = (x + y)
    if len(x) == len(y):
        c = sorted([x*y for x,y in zip(x,y)])
    else:
        c = sorted([j for j in z if z.count(j) > 1])
    return c
assert(foo([1, 2, 3, 3, 3], [-1, 2, 3])) == [2, 2, 3, 3, 3, 3]
assert(foo( [1, 2, 3],[-1, 2, 0])) == [-1,0,4]
assert(foo([0,0,1, 0, 11, 8, 9], [-1,-2,-3,-4,-5,-7])) ==[0,0,0]
