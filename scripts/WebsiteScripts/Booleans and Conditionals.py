import random

#@ @3@ @1@ @case2@ @case3@ @case1@
x = 2
y = 4
z = 9
if x <= 2 and y > 4:
    print('case1')
elif z < 9 or x >= 2:
    print('case2')
else:
    print('case3')

#@ @3@ @2@ @10@ @1@ @2@ @8@ @5@
count = 0
x = 'A'
y = 'B'
if x == 'X' or y == x:
    count += 1
elif count < 50 and y == 'B':
    count += 5
else:
    count *= 3
count *= 2
print(count)

#@ @3@ @3@ @0@ @Impossible to Determine@ @1@ @50@
num = random.randint(0,1)
if num == 0:
    print(num)
elif num == 1:
    print(num - 1)
else:
    print(50)

#@ @3@ @4@ @False True@ @False False@ @True True@ @True False@
x = 1
y = '1'
a = x == y and x > 0
b = y != '1' or x % 5 >= 1
print(a, b)

#@ @3@ @5@ @True True@ @True False@ @False True@ @False False@ @Impossible to determine@
x = random.randint(5, 10)
y = x == 7 or not '1' == 1
z = 42
a = y and z > x
print(y, a)

#@ @3@ @6@ @False False@ @False True@ @True False@ @True True@
x = 501
y = 500
z = 5
p = y % z == 0 and not (y + z > x or x // z == 0)
q = not (z > x - y and x % y == 1)
print(p, q)