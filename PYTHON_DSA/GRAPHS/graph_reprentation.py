
edges = [[1,2], [2,4], [3,4], [1,3], [3,5], [5,4]]
n = len(edges)

## Matrix
matrix = [[0]*n for _ in range(n)]

for u, v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1

print(matrix)
for row in matrix:
    print(row)

## List
lst = [[] for _ in range(n+1)]

for u, v in edges:
    lst[u].append(v)
    lst[v].append(u)

# print(lst)

## Dictionary
mydict = {}

for i in range(1, n+1):
    mydict[i] = []

for u, v in edges:
    mydict[u].append(v)
    mydict[v].append(u)

# print(mydict)