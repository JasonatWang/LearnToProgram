from numpy import *
n = eval(input('请输入关系矩阵的阶: '))
print('关系矩阵是', n, '阶矩阵\n请输入关系矩阵: ')
a = list()
for row in range(n):
    a.append(input().split(' '))
# 转化为矩阵
matA = mat(a)

# test
print(matA)
print(matA[1, 2])