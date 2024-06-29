def count_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

print(count_factors(12))
print(count_factors(15))
print(count_factors(17))

def second_half_letters(phrase):
    count = 0
    # Convert to lower case so we only have to check [n, z]
    phrase = phrase.lower()
    for char in phrase:
        if 'n' <= char <= 'z':
            count += 1
    return count

print(second_half_letters('Nasir Ahmed'))
print(second_half_letters('David Huffman'))
print(second_half_letters('Claude Shannon'))


def percent_even(data):
    count = 0
    for i in range(len(data)):
        if data[i] % 2 == 0:
            count += 1

    if len(data) == 0:
        return 0.0
    else:
        return 100.0 * count / len(data)

print(percent_even([6, 2, 9, 11, 3]),
percent_even([2]),
percent_even([11, 19, 5, 97]))


def mirror(data):
    for i in range(len(data) - 1, -1, -1):
        data.append(data[i])

x = ['a','b','c']
mirror(x)
print(x)

x = [5, 9, 1]
mirror(x)
print(x)

x = ['a']
mirror(x)
print(x)


def replace(source, target, replacement):
    result = ''
    for ch in source:
        if ch == target:
            result += replacement
        else:
            result += ch
    return result


print(replace('Larry', 'r', 'great'))
print(replace('Tim', 't', 'J'))
print(replace('CS303E', '0', '1'))


def contains_all(data1, data2):
    for i in range(len(data1)):
        found = False
        j = 0
        while not found and j < len(data2):
            found = data1[i] == data2[j]
            j += 1
        if not found:
            return False
    return True


print(contains_all([-5, 0, -5, 2, -5], [2, 0, -5, 12]))
print(contains_all([], [2]))
print(contains_all([0, 5, 1, 17], [1, 0, 17, 17, -5, 15]))


def reverse_columns(data):
    result = []
    for r in range(len(data)):
        result.append([])
        row_in_data = len(data) - 1 - r
        for c in range(len(data[r])):
            result[r].append(data[row_in_data][c])
    return result


print(reverse_columns([[0, 13, 12],
                       [4, 72, 17],
                       [9, 60, 15]]))

# [[9, 60, 15],
#  [4, 72, 17],
#  [0, 13, 12]]


print(reverse_columns([[32, 341, 2],
                       [23, 722, 1],
                       [49, 453, 5],
                       [13, 234, 3]]))


# [[13, 234, 3],
#  [49, 453, 5],
#  [23, 722, 1],
#  [32, 341, 2]]


print(reverse_columns([[0, 1, 2, 3, 4],
                       [5, 6, 7, 8, 9]]))

# [[5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4]]

def swap_matrices(data1, data2):
    for r in range(len(data1)):
        for c in range(len(data1[r])):
            if data1[r][c] % 2 == data2[r][c] % 2:
                data1[r][c], data2[r][c] = data2[r][c], data1[r][c]



x = [[0, 13, 12],
     [4, 72, 17],
     [9, 60, 15]]

y = [[2, 19, 21],
     [8, 71, 19,],
     [11, 22, 26]]

print(x)
print(y)


swap_matrices(x, y)


print(x)
print(y)





