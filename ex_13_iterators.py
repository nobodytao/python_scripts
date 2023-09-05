numbers=[1,2,3,4,5]
i = iter(numbers)

print(next(i))
print(next(i))

f = open('r1.txt','r')

print(f.__next__())

genexpr = (x**2 for x in range(3))

print(genexpr.__next__())
print(genexpr.__next__())
print(next(genexpr))
