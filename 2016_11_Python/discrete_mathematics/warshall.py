from numpy import *


# WarShall算法
def war_shall(mat_a, n):
    for k_num in range(n):
        for row_num in range(n):
            for col_num in range(n):
                mat_a[row_num, col_num] =\
                    mat_a[row_num, col_num] or (mat_a[row_num, k_num] and mat_a[k_num, col_num])
    return mat_a


# 输入关系矩阵
def input_matrix():
    # 输入矩阵
    n = eval(input('请输入关系矩阵的阶: '))
    print('关系矩阵是', n, '阶矩阵\n请输入关系矩阵: ')
    a = list()
    for row in range(n):
        a.append(list(map(int, input().split(' '))))

    # 将得到的输入值转化为矩阵
    mat_a = array(a)
    return mat_a, n


# 输出关系矩阵
def output_matrix(mat_x, name_str):
    print(name_str, ':')
    for row in mat_x:
        for col in row:
            print(col, end=' ')
        print()


def main():
    mat_a, n = input_matrix()
    t_mat_a = war_shall(mat_a, n)

    # 输出
    output_matrix(mat_a, '输入的关系矩阵')
    output_matrix(t_mat_a, '传递闭包的关系矩阵')

if __name__ == '__main__':
    main()
