from numpy import *


# WarShall算法
def war_shall(mat_a, n):
    for k_num in range(n):
        for row_num in range(n):
            for col_num in range(n):
                mat_a[row_num, col_num] =\
                    mat_a[row_num, col_num] or (mat_a[row_num, k_num] and mat_a[k_num, col_num])
    return mat_a


# 把关系矩阵转化为表示关系的字典
def transfer_mat_to_letter(mat_x, n):
    num_to_letter = dict(zip([num for num in range(n)], 'abcdefghijklmnopqrstuvwxyz'[:n]))
    relation_dict = dict()
    multi_sign = '0'
    for row_num in range(n):
        for col_num in range(n):
            if mat_x[row_num, col_num]:
                if num_to_letter[row_num] in relation_dict:
                    num_to_letter[row_num] += multi_sign
                    multi_sign += '0'
                relation_dict.update({num_to_letter[row_num]: num_to_letter[col_num]})
    return relation_dict


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


# 输出关系
def output_relationship(relation_dict, name_str):
    print('{0}关系为:'.format(name_str))
    print('{', end='')
    for keys in relation_dict:
        print('<', keys[:1], ',', relation_dict[keys][:1], '>,', end=' ')
    print('\b\b}')


def main():
    mat_a, n = input_matrix()
    i_mat_a = mat_a.copy()
    # 输出输入矩阵
    output_matrix(i_mat_a, '输入的关系矩阵')
    # WarShall算法
    t_mat_a = war_shall(mat_a, n)
    # 输出传递闭包
    output_matrix(t_mat_a, '传递闭包的关系矩阵')

    relationship = transfer_mat_to_letter(i_mat_a, n)
    output_relationship(relationship, '输入')
    t_relationship = transfer_mat_to_letter(t_mat_a, n)
    output_relationship(t_relationship, '传递闭包')

if __name__ == '__main__':
    main()