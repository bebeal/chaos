#@ @4@ @1@ @0@ @2@ @20@ @1024@
count = 0
for i in range(0, 10):
    count *= 2
print(count)

#@ @4@ @2@ @4@ @3@ @5@ @10@ @6@
loop_control = 1
count = 0
while loop_control < 10:
    loop_control *= 2
    count += 1
print(count)

#@ @4@ @3@ @49@ @RUNTIME ERROR@ @1@ @50@
what_am_i = 0
for i in range(50):
    what_am_i = i
print(what_am_i)


#@ @4@ @4@ @50@ @49@ @48@ @51@
loop_control = -2
while loop_control < 50:
    loop_control += 1
print(loop_control)

#@ @4@ @5@ @8@ @12@ @4@ @15@ @3@
count = 0
for i in range(3, 15, 3):
    count += 2
print(count)

#@ @4@ @6@ @INFINITE LOOP@ @0@ @1@ @20@
loop_control = -10
while loop_control <= 0:
    loop_control *= 2
print(loop_control)

#@ @4@ @7@ @10@ @INFINITE LOOP@ @0@ @11@ @9@
count = 0
for i in range(10, 0, -1):
    count += 1
print(count)

#@ @4@ @8@ @7@ @14@ @21@ @2@
count = 0
for i in range(7):
    for j in range(2):
        count += j
print(count)