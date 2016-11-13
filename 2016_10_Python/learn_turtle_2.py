import turtle
import numbers
def draw_tree(trees,a=45,l=100):
    if l>10:
        lstree=[]
        for tree in trees:
            tree_2=tree.clone()
            tree.lt(a)
            tree_2.rt(a)
            tree.fd(l)
            tree_2.fd(l)
            lstree.append(tree_2)
        l *=0.7
        trees=trees+lstree
        draw_tree(trees,30,l)
def plant_tree(x,y,h):
    turtle.title("Jason Wang -> 画树").speed(30)
    turtle.pensize(10)
    turtle.shape("classic")
    turtle.color("DeepSkyBlue")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.lt(90)
    turtle.fd(h)
    tree_lt = turtle
    tree_rt = tree_lt.clone()
    trees = [tree_lt, tree_rt]
    draw_tree(trees, 45, 150)
# plant_tree(0,-300,200)
turtle.title("Jason Wang -> 显示时间")
turtle.speed(1)
turtle.pensize(10)
turtle.shape("turtle")
turtle.color("DeepSkyBlue")
x1=-450
dx=100
num=turtle
numbers.show_time(num,x1,0,dx)