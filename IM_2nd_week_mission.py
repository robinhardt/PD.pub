# [이벤트 처리]
## turtle 마우스 이벤트 처리 연습문제
## : 마우스로 랜덤한 turtle 스탬프를 찍는 프로그램을 작성해보자.

'''
import turtle as t
import random

# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

# turtleStamp 핸들링 함수: 거북이 스탬프 모양을 찍는 함수
def turtleStamp(x, y):
    t.hideturtle()                                      # 거북이 숨기기
    t.goto(x, y)                                        # (x,y)좌표로 거북이 이동
    t.setheading(random.randint(0, 360))                # 랜덤하게 거북이의 머리 방향 지정(0~360도)
    t.shapesize(random.randint(1, 10))                  # 랜덤하게 거북이의 크기 설정(1~10)
    r, g, b = randomColor()                             # 랜덤 r,g,b 값 가져오기(randomColor 함수 사용하기)
    t.fillcolor(r, g, b)                                # 스템프 색상 설정(랜덤 r,g,b 값 넣기)
    t.pencolor(r, g, b)                                 # 스템프 테두리 색성 설정(랜덤 r,g,b 값 넣기)
    t.stamp()                                           # 스템프 찍기 명령


t.title('거북이 도장 찍기')                                # 제목 달기 "거북이 도장 찍기"
t.shape('turtle')                                       # 도장 모양을 turtle으로 설정
t.speed(0)                                              # 속도 설정
t.penup()                                               # 펜 들기

# 왼쪽 마우스 클릭 시, 스탬프 찍기
t.onscreenclick(turtleStamp, 1)
t.mainloop()

'''

## turtle 마우스 이벤트 처리 Mission
## : 오른쪽 마우스 클릭 시 화면이 지워지는 기능을 추가해보자.
## turtle 마우스 이벤트 처리 Mission

import turtle as t
import random

# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

# turtleStamp 핸들링 함수: 거북이 스탬프 모양을 찍는 함수
def turtleStamp(x, y):
    t.hideturtle()                                      # 거북이 숨기기
    t.goto(x, y)                                        # (x,y)좌표로 거북이 이동
    t.setheading(random.randint(0, 360))                # 랜덤하게 거북이의 머리 방향 지정(0~360도)
    t.shapesize(random.randint(1, 10))                  # 랜덤하게 거북이의 크기 설정(1~10)
    r, g, b = randomColor()                             # 랜덤 r,g,b 값 가져오기(randomColor 함수 사용하기)
    t.fillcolor(r, g, b)                                # 스템프 색상 설정(랜덤 r,g,b 값 넣기)
    t.pencolor(r, g, b)                                 # 스템프 테두리 색성 설정(랜덤 r,g,b 값 넣기)
    t.stamp()                                           # 스템프 찍기 명령

def turtleclear(x, y):
    t.clear()


t.title('거북이 도장 찍기')                                # 제목 달기 "거북이 도장 찍기"
t.shape('turtle')                                       # 도장 모양을 turtle으로 설정
t.speed(0)                                              # 속도 설정
t.penup()                                               # 펜 들기

# 왼쪽 마우스 클릭 시, 스탬프 찍기
t.onscreenclick(turtleStamp, 1)
t.onscreenclick(turtleclear, 3)

t.mainloop()

## turtle 키보드 이벤트 처리 연습문제
'''
import turtle as t
import random

# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

# 방향키 위를 눌렀을 때의 핸들링 함수
def up():
    t.setheading(90)                                # 가려는 방향에 맞게 방향설정
    r, g, b = randomColor()                         # 랜덤 색상 r,g,b 가져오기
    t.pencolor(r, g, b)                             # 펜 색상 설정
    t.fillcolor(r, g, b)                            # 거북이의 색상도 같이 설정
    t.forward(10)                                   # 10만 큼 이동

# 방향키 아래키를 눌렀을 때의 핸들링 함수
def down():
    t.setheading(270)
    r, g, b = randomColor()
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)
    t.forward(10)


t.title('마리오의 별을 훔쳐먹은 거북이')                     # 제목 설정 "마리오의 별을 훔쳐먹은 거북이"
t.bgcolor('black')                                      # 배경색을 검정(black)으로 설정하기
t.shape('turtle')                                       # 모양을 'turtle'로 설정
t.pensize(10)                                           # 펜사이즈 10 설정

t.onkeypress(up, 'Up')                                    # up 이벤트 설정
t.onkeypress(down, 'Down')                                # down 이벤트 설정
t.listen()                                              # listen을 실행시켜 주어야 키 입력 모두가 실행되어 입력키에 반응함.

t.mainloop()
'''

## turtle 키보드 이벤트 처리 Mission
import turtle as t
import random
import pygame

# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

# 방향키 위를 눌렀을 때의 핸들링 함수
def up():
    t.setheading(90)                                # 가려는 방향에 맞게 방향설정
    r, g, b = randomColor()                         # 랜덤 색상 r,g,b 가져오기
    t.pencolor(r, g, b)                             # 펜 색상 설정
    t.fillcolor(r, g, b)                            # 거북이의 색상도 같이 설정
    t.forward(10)                                   # 10만 큼 이동

# 방향키 아래키를 눌렀을 때의 핸들링 함수
def down():
    t.setheading(270)
    r, g, b = randomColor()
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)
    t.forward(10)

def right():
    t.setheading(0)
    r, g, b = randomColor()
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)
    t.forward(10)

def left():
    t.setheading(180)
    r, g, b = randomColor()
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)
    t.forward(10)

def clearbg():
    t.clear()

def escape():
    t.bye()

pygame.init()

t.title('마리오의 별을 훔쳐먹은 거북이')                     # 제목 설정 "마리오의 별을 훔쳐먹은 거북이"
t.bgcolor('black')                                      # 배경색을 검정(black)으로 설정하기
t.shape('turtle')                                       # 모양을 'turtle'로 설정
t.pensize(10)                                           # 펜사이즈 10 설정

bgm = pygame.mixer.Sound("C:/Users/binip/PycharmProjects/PD.pub/Star.mp3")
bgm.play(-1)

t.onkeypress(up, 'Up')                                    # up 이벤트 설정
t.onkeypress(down, 'Down')                                # down 이벤트 설정
t.onkeypress(right, 'Right')
t.onkeypress(left, 'Left')
t.onkeypress(clearbg, 'space')
t.onkeypress(escape, 'Escape')
t.listen()                                              # listen을 실행시켜 주어야 키 입력 모두가 실행되어 입력키에 반응함.

t.mainloop()


# [Tkinter]
## Tkinter 시작하기


## Tkinter 시작하기: Window 창 설정하기


## Tkinter 위젯: Label() - 1
## Hello World를 포함한 GUI창 띄우기


## Tkinter 위젯: Label() - 1 변형
## Hello World를 포함한 GUI창 띄우기 + (koverwatch,50)으로 font 바꿔보기


## Tkinter 위젯 배치 관리자 연습문제


## Tkinter 위젯: PhotoImage()
## 저장된 이미지를 GUI화면에 출력해보자.

