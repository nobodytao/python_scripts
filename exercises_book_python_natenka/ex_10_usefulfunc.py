numbers = [1,2,3,4,5]
numbers2 = ['11','22','33','44','55']

s = zip(numbers,numbers2)

for p,s in enumerate(s):
    print(p,s)

print(all(item.isdigit() for item in numbers2))

mult = lambda a,b,c: a*b+c

print(mult(10,2,2))

list_of_tuples = [('IT_VLAN', 320),
('Mngmt_VLAN', 99),
('User_VLAN', 1010),
('DB_VLAN', 1100)]

print (sorted(list_of_tuples, key=lambda x: x[1]))

print(list(map(lambda a,b: "{1}+{0}".format(a,b),numbers,numbers2)))