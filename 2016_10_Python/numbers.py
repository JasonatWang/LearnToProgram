import turtle
def circles_rt(num,times,len,seth=90):
    for i in range(times):
        num.rt(seth)
        num.fd(len)
def circles_lt(num,times,len,seth=90):
    for i in range(times):
        num.lt(seth)
        num.fd(len)
def strings(num,x,str,y=0):
    moved(x,y-50)
    num.write(str, move=False, align="center", font=("Microsoft YaHei", 50, "normal"))
    moved()
def num_0(num,x,y=0):
    moved(x,y)
    circles_lt(num,1,50)
    circles_rt(num,2,50)
    num.fd(50)
    circles_rt(num,2,50)
    moved()
def num_1(num,x,y=0):
    moved(x+50,y+50)
    circles_rt(num,1,100)
    moved()
def num_2(num,x,y=0):
    moved(x,y)
    num_down=num.clone()
    circles_rt(num_down,1,50)
    circles_lt(num_down,1,50)
    num.fd(50)
    circles_lt(num,2,50)
    moved()
def num_3(num,x,y=0):
    moved(x,y)
    num.fd(50)
    num_lt=num.clone()
    circles_lt(num_lt,2,50)
    circles_rt(num,2,50)
    moved()
def num_4(num,x,y=0):
    moved(x,y)
    num_up=num.clone()
    circles_lt(num_up,1,50)
    num.fd(50)
    num_lt=num.clone()
    circles_lt(num_lt,1,50)
    circles_rt(num,1,50)
    moved()
def num_5(num,x,y=0):
    moved(x,y)
    num_up=num.clone()
    circles_lt(num_up,1,50)
    circles_rt(num_up,1,50)
    num.fd(50)
    circles_rt(num,2,50)
    moved()
def num_6(num,x,y=0):
    moved(x,y)
    num.fd(50)
    circles_rt(num,3,50)
    num.fd(50)
    circles_rt(num,1,50)
    moved()
def num_7(num,x,y=0):
    moved(x+50,y+50)
    num_lt=num.clone()
    circles_lt(num_lt,1,50,180)
    circles_rt(num,1,100)
    moved()
def num_8(num,x,y=0):
    moved(x,y)
    circles_lt(num,1,50)
    circles_rt(num,2,50)
    num.fd(50)
    circles_rt(num,2,50)
    circles_rt(num,1,50)
    moved()
def num_9(num,x,y=0):
    moved(x,y)
    num.fd(50)
    num_down=num.clone()
    circles_rt(num_down,1,50)
    circles_lt(num,3,50)
    moved()
def moved(x=0,y=0):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.seth(0)
def show_time(num,x,y,dx):
    times=input("Input Time Here: ")
    i=0
    for time in times:
        if time == '0':
            num_0(num,x,y)
        elif time == '1':
            num_1(num, x, y)
        elif time == '2':
            num_2(num, x, y)
        elif time == '3':
            num_3(num, x, y)
        elif time == '4':
            num_4(num, x, y)
        elif time == '5':
            num_5(num, x, y)
        elif time == '6':
            num_6(num, x, y)
        elif time == '7':
            num_7(num, x, y)
        elif time == '8':
            num_8(num, x, y)
        elif time == '9':
            num_9(num, x, y)
        x += dx
        i += 1
        if i == 4:
            strings(num, x, " 年 ", y)
            x += dx
        elif i==8:
            strings(num, x, " 日 ", y)