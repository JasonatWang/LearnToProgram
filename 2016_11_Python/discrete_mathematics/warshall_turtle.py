from numpy import *
import turtle


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


# 将turtle移动到特定位置, 并把箭头指向恢复
def moved(x=0, y=0):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.seth(0)


# 画线
def draw_lines(letter_dict, relation):
    for keys, values in relation.items():
        from_position = letter_dict[keys[:1]].pos()
        to_position = letter_dict[values[:1]].pos()
        moved(from_position[0], from_position[1])
        if from_position == to_position:
            turtle.color("LightSkyBlue")
            turtle.circle(50)
            turtle.color("DeepSkyBlue")
        elif from_position[0] < to_position[0]:
            turtle.seth(270)
            turtle.color("CornflowerBlue")
            turtle.circle((to_position[0] - from_position[0]) / 2, 180)
            turtle.color("DeepSkyBlue")
        else:
            turtle.seth(90)
            turtle.circle((from_position[0] - to_position[0]) / 2, 180)
        moved(0, 0)


# 画图
def draw_schema(letters_to_write, relation, n):
    num_to_letter = dict(zip([num for num in range(n)], 'abcdefghijklmnopqrstuvwxyz'[:n]))
    letters_set = set()
    x = -500
    dx = 200
    dot_dict = dict()
    for num in range(n):
        letters_set.add(num_to_letter[num])
    for letter in letters_set:
        x += dx
        moved(x)
        dot_dict.update({letter: letters_to_write.clone()})
        letters_to_write.dot(15, "Indigo")
        letters_to_write.color("Indigo")
        letters_to_write.write(letter, move=False, align="left", font=("Microsoft YaHei", 20, "normal"))
        letters_to_write.color("DeepSkyBlue")
        moved(0, 0)
    draw_lines(dot_dict, relation)


# 画关系图主程序
def draw_relation_schema(relation, n):
    turtle.title("离散闭包关系图 code by 王霄")
    turtle.speed(3)
    turtle.pensize(5)
    turtle.shape("classic")
    turtle.color("DeepSkyBlue")
    letters_to_write = turtle
    draw_schema(letters_to_write, relation, n)
    turtle.done()


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


# 主程序 code by 王霄 ~
def main():
    mat_a, n = input_matrix()
    i_mat_a = mat_a.copy()
    # 输出输入矩阵
    output_matrix(i_mat_a, '输入的关系矩阵')
    # WarShall算法
    t_mat_a = war_shall(mat_a, n)
    # 输出传递闭包
    output_matrix(t_mat_a, '传递闭包的关系矩阵')

    relation = transfer_mat_to_letter(i_mat_a, n)
    output_relationship(relation, '输入')
    t_relation = transfer_mat_to_letter(t_mat_a, n)
    output_relationship(t_relation, '传递闭包')

    # 画关系图
    draw_relation_schema(t_relation, n)

    input("按任意键退出")


if __name__ == '__main__':
    main()