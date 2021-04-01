x = int(input())
# размер матрицы х*х
matrix = [[0] * x for i in range(x)]
# сама матрица
digit = 1
# счетчик
y = 0
matrix[x//2][x//2] = x * x
# Центральный элемент
for j in range(x//2):
    #верхняя часть матрицы
    for i in range(x-y):
        matrix[j][i+j] = digit
        digit +=1
    for i in range(j + 1,x - j):
        matrix[i][-j-1] = digit
        digit += 1
    for i in range(j + 1, x - j):
        matrix[-j - 1][-i-1] = digit
        digit += 1
    for i in range(j + 1, x - (j+1)):
        matrix[-i-1][j] = digit
        digit += 1
    y += 2
for i in matrix:
    print(*i)