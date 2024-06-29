#@ @10@ @1@ @{'z': 5, 'a': 7, 'm': 7}@ @{'z': 5, 'a': 5, 'm': 7}@ @{'z': 5, 'a': 8, 'm': 7}@ @{5: 'z', 7: 'a', 7: 'm'}@ @{5: 'z', 8: 'a', 7: 'm'}@
x = {}
x['z'] = 5
x['a'] = 8
x['m'] = 7
x['a'] = x['z'] + 2
print(x)

#@ @10@ @2@ @{12: 'D', 5: 'A', -5: 'A', 0: 'D'}@ @{'D': 12, 'A': 5, 'A': -5, 'D': 0}@ @{12: 'M', 5: 'A', -5: 'A', 0: 'M'}@ @{'D': 12, 'A': -5, 'D': 0}@
m = {}
m[12] = 'M'
m[5] = 'A'
m[12] = 'D'
m[-5] = 'A'
m[0] = m[12]
print(m)

#@ @10@ @3@ @{35: 0, 90: 1, 1: 2, 23: 3, 4: 4, 52: 5}@ @{0: 35, 1: 90, 2: 1, 3: 23, 4: 4, 5: 52}@
wow = [35, 90, 1, 23, 4, 52]
m = {}
for i in range(len(wow)):
    m[wow[i]] = i
print(m)

#@ @10@ @4@ @TACC Sequoia Roadrunner Titan@ @1, 4, 2, 3@
m = {'TACC': 1, 'Sequoia': 4, 'Roadrunner': 2, 'Titan': 3}
for key in m:
    print(key, end=' ')

#@ @10@ @5@ @370.46 125.79 201.3@ @Apple, IBM, Microsoft@ @125.79, 370.46, 201.30@ @IBM Apple Microsoft@
m = {'IBM': 125.79, 'Apple': 370.46, 'Microsoft': 201.30}
for key in sorted(m.keys()):
    print(m[key], end=' ')