import turtle
def draw_snake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle / 2)
    turtle.fd(rad)
    turtle.circle(neckrad + 1, 180)
    turtle.fd(rad * 2 / 3)
def draw_tangle(length,seths):
    for i in range(3):
        turtle.fd(length)
        turtle.seth(seths)
        seths +=seths
def main():
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 20
    turtle.pensize(pythonsize)
    turtle.pencolor("lightgreen")
    turtle.seth(0)
    # draw_snake(40, 80, 5, pythonsize / 2) 画蛇
    draw_tangle(100,120) #画三角
main()