#@ @2@ @1@ @-23 4@ @23 -4@ @RUNTIME ERROR@ @4 -23@
x = eval('4')
y = int('-23')
print(y, x)

#@ @2@ @2@ @10@ @9 + 1@ @RUNTIME ERROR@ @10.0@
a = eval('9 + 1')
print(a)

#@ @2@ @3@ @RUNTIME ERROR@ @1 - 1@ @0@ @0.0@
t = int('1 - 1')
print(t)

#@ @2@ @4@ @100.0@ @RUNTIME ERROR@ @100@
k = eval('99.0 + 1')
print(k)

#@ @2@ @5@ @['A', 'l', 'a', 'n', ' ', 'T', '.']@ @['Alan T.']@ @RUNTIME ERROR@ @['Alan', 'T.']@
l = list('Alan T.')
print(l)

#@ @2@ @6@ @6@ @4@ @7@ @6 7@
x = min(max(3, 6), max(4, 7))
print(x)