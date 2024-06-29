#@ @7@ @1@ @[1, 0, 10, 0, 0, 1]@ @[1, 0, 0, 10, 0, 0, 1]@ @[1, 0, 0, 10, 0, 1]@ @[1, 0, 10, 0, 1]@
x = [0, 0, 0, 0]
x.append(1)
x.insert(2, 10)
x[0] = 1
print(x)

#@ @7@ @2@ @[0, 0, 1, 2, 3]@ @[1, 2, 3, 4, 5]@ @[0, 1, 2, 3, 4]@ @[0, 0, 1, 2, 3, 4]@
x = []
for i in range(5):
    x.append(i)
    for j in range(i):
        x[i] = j
print(x)

#@ @7@ @3@ @[3, 3, 3]@ @[3, 1, 4, 1, 5, 9]@ @[0, 1, 2]@ @[3, 1, 4, 1, 5, 9, 3, 3, 3]@
x = [3, 1, 4, 1, 5, 9]
def make_list(num):
    y = []
    for i in range(num):
        y.append(num)
    return y
x = make_list(3)
print(x)

#@ @7@ @4@ @50@ @SYNTAX ERROR@ @1@ @0@
x = [3] * 50
print(len(x))

#@ @7@ @5@ @[0, 0, 0, 0, 0, 5, 6, 7]@ @[0, 0, 0, 0, 0, 5, 5, 5]@ @RUNTIME ERROR@
x = [0, 0, 0, 0, 0]
for i in range(3):
    x.append(len(x))
print(x)

#@ @7@ @6@ @SYNTAX ERROR@ @[4, 0]@ @[4, 4]@ @[0, 0]@ @[0, 4]@
x = [0]
x.index(0) = 4
x.append(x.index(4))
print(x)

#@ @7@ @7@ @11@ @10@ @0@ @1@
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for i in range(len(x)):
    if x[i] == count:
        count += 1
print(count)

#@ @7@ @8@ @[0, 0]@ @SYNTAX ERROR@ @[1, 0]@ @[0, 1]@
x = []
x.insert(0, len(x))
x.append(x.index(0))
print(x)

#@ @7@ @9@ @[6, 8, 1, 2, 8, 2]@ @[2, 1, 0, 5, 4, 3]@ @[1, 8, 6, 2, 8, 2]@ @[2, 8, 2, 6, 8, 1]@ @[0, 1, 2, 3, 4, 5]@
x = [1, 8, 6, 2, 8, 2]
y = [2, 1, 0, 5, 4, 3]
z = []
for num in y:
    z.append(x[num])
print(z)

#@ @7@ @10@ @[50, 1, 0]@ @[0]@ @[0, 1]@ @[50, 1]@ @[0, 0, 0]@ @[]@ @[0, 0, 0, 3]@ @[50, 1, 0, 3]@
x = []
def foo(a):
    a.append(len(a))
    a = bar(a)
    a.append(len(a))
    return a
def bar(b):
    b.append(len(b))
    b[0] = 50
    b.append(0)
    b = [0, 0, 0]
    return b
foo(x)
print(x)

#@ @7@ @11@ @34@ @RUNTIME ERROR@ @12@ @40@ @16@
x = [6, 2, 4, 5, 6, 1, 4, 0]
count = 0
for num in x:
    count += x[num % 5]
print(count)

#@ @7@ @12@ @[1, -4, 3, 5, 2] [1, -4, 3, 5, 2]@ @[1, -4, 3, 5, 6] [1, 9, 3, 5, 2]@ @[1, -4, 3, 5, 6] [1, 9, 3, 5, 2]@
x = [1, 9, 3, 5, 6]
y = x
y[4] = 2
x[1] = y[3] - x[1]
print(x, y)