#@ @8@ @1@ @[[0, -1, -2], [1, 0, -1], [2, 1, 0]]@ @[[0, 1, 2], [-1, 0, 1], [-2, -1, 0]]@ @[[1, -2, -3], [2, 1, -2], [3, 2, 1]]@ @[[-1, 2, 3], [-2, -1, 2], [-3, -2, -1]]@
mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for r in range(len(mat)):
    for c in range(len(mat[r])):
        mat[r][c] = r - c
print(mat)

#@ @8@ @2@ @[[0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 0, 0], [1, 0, 1, 0]]@ @[[0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0], [0, 1, 0, 1]]@ @[[1, 0, 1, 0], [0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 0, 0]]@ @[[0, 1, 0, 1], [0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0]]@
mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for r in range(len(mat)):
    for c in range(len(mat[r])):
        if r % 2 == 1 and c % 2 == 0:
            mat[r][c] = 1
print(mat)

#@ @8@ @3@ @[[], [1], [2, 3]]@ @[[0], [1, 2], [3, 4, 5]]@ @RUNTIME ERROR@ @[[], [0], [1, 2]]@
mat = []
for i in range(3):
    mat.append([])
    for j in range(i):
        mat[i].append(j + i)
print(mat)

#@ @8@ @4@ @8@ @RUNTIME ERROR@ @11@ @2@ @3@ @4@
count = 0
mat = [[4, 5, 2],
       [2, 0, 7],
       [0, 9, 4]]
for i in range(len(mat)):
    count += mat[i][i]
print(count)

#@ @8@ @5@ @21@ @5@ @7@ @16@
count = 0
mat = [[-7, -1, 5],
       [2, 9, -2],
       [-4, 7, 6]]
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if j < i:
            count += mat[i][i]
print(count)
