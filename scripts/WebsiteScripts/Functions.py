#@ @5@ @1@ @18@ @9@ @11@ @0@ @2@
def a(x, y):
    x = 3
    y = 3
    return x * y

def b(z, t):
    z += 2
    t = a(z, t)
    return z * t

what_am_i = b(0, 0)
print(what_am_i)

#@ @5@ @2@ @12@ @9@ @7@ @0@ @10@
def a(x):
    x = b(x)
    return x + 2

def b(y):
    return y * 2

what_am_i = a(5)
print(what_am_i)

#@ @5@ @3@ @1 50 0@ @1 0 1@ @50 50 0@ @50 0 1@
def a(x, y):
    return x + y

def b(z, t):
    z = 0
    t = 1
    return a(z, t)

z = 50
t = 0
print(b(z, t), z, t)

#@ @5@ @4@ @LISP ['BASIC', 'COBOL']@ @LISP Algol ['BASIC', 'COBOL']@ @LISP ['BASIC']@
def add_more(s, d):
    s += ' Algol'
    d.append('COBOL')
    return s, d

s = 'LISP'
d = ['BASIC']
add_more(s, d)
print(s, d)