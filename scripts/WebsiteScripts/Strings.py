#@ @6@ @1@ @Boolean Zen.@ @ @ @RUNTIME ERROR@ @ Zen.@ @Boolean@
s1 = 'Boolean'
s2 = '.'
if len(s1) == 7:
    s1 += ' Zen'
s1 = s1 + s2
print(s1)

#@ @6@ @2@ @1JVN1JVN@ @RUNTIME ERROR@ @1JVN1@ @VJVNVJVN@
s = 'JVN'
s2 = str(1) + s + str(1)
print(s2 + s)

#@ @6@ @3@ @10@ @RUNTIME ERROR@ @0@ @25@
s = ''
for i in range(5):
    s += ' ' * i
print(len(s))

#@ @6@ @4@ @RUNTIME ERROR@ @Ten10@
s = 'Ten' + 10
print(s)

#@ @6@ @5@ @RAN JWB FOR@ @RUNTIME ERROR@ @FOR JWB RAN@ @AN JWB FOR@
s1 = 'FORTRAN'
s2 = 'JWB'
y = s1[4:]
x = s2[:3]
z = s1[:3]
print(y, x, z)

#@ @6@ @6@ @e@ @RUNTIME ERROR@ @Flourless Chocolate Cake@ @@
s1 = 'Flourless Chocolate Cake'
x = s1[-1:50]
y = s1[50:-100]
print(x, y)

#@ @6@ @7@ @RUNTIME ERROR@ @JAVA@ @JAV@ @C++A@
s = 'C++'
s[0] = 'J'
s[1] = 'A'
s[2] = 'V'
s += 'A'
print(s)

#@ @6@ @8@ @Turtles All The Way Down@ @... you forgot the elephants@ @Turtles All The Way Down... you forgot the elephants@
s = 'Turtles All The Way Down'

def foo(s):
    s = '... you forgot the elephants'
    return s

foo(s)
print(s)

#@ @6@ @9@ @EWD EAE EAE EWD@ @EWD EAE EWD EAE@ @EAE EWD EWD EAE@ @EAE EWD EAE EWD@
s1 = 'EWD'
s2 = 'EAE'

def bar(s1, s2):
    print(s1, s2, end=' ')
    s2, s1 = s1, s2
    return s2, s1

s2, s1 = bar(s1, s2)
print(s1, s2)