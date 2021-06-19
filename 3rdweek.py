# name = input("이름을 입력해주세요")
# print("%s님 안녕하세요" %name)

#등산
import turtle
win = turtle.Screen()
turtle.setup(800,600)
turtle.title("거북이 등산")
win.bgpic("산길.gif")
t = turtle.Turtle("turtle")
t.penup()
t.goto(-100, -250)
t.left(30)
t.forward(200)
t.setheading(90)
t.forward(10)
t.setheading(150)
t.forward(100)

turtle.mainloop()