# 4주차 mission
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!

[3주차 복습]
1. Github에 commit, push 하기
2. 주석 처리 하는 방법 2가지
3. 문자열 입출력 print(), input()
'''

''' print("Hello, World!")'''

# [자료형]
## 숫자형 1) 정수형(integer, int)
## : 소수점이 없는 숫자의 형태
## mission>> 정수형인 숫자를 출력하고 type() 함수를 활용하여 자료형을 주석으로 적기

'''print(5, 5, 5, 5)
print(type(5))'''          # int


# 숫자형 2) 실수형(float)
## : 소수점이 있는 숫자의 형태
## mission>> 실수형인 숫자를 출력하고 type() 함수를 활용하여 자료형을 주석으로 적기

'''print(5.55555)
print(type(5.55555))'''    #float


## 문자열
## : 문자를 나열한 형태의 자료형
## mission1>> ""와 ''를 활용하여 내가 지금 하고 싶은 말을 문자열로 출력하기

'''print("집에 보내줘....")
print('갓챠')'''

## mission2>> 문자열로 인용구호('') 출력하기

'''print('"멈춰!"라고 말했다.')'''

## mission3>> sep과 end를 활용하여 print() 용법 익히기
## sep: ,로 출력이 구분된 문자열 사이 출력 설정 // end: print문의 끝났을 때의 문자열 출력 설정

'''print(1,2,3,4,5,6, sep='/', end='콩진호')
print(1,2,3,4,5,6, sep='/', end='콩진호')
'''

## - 불린형(참/거짓)
## : 참(True)/거짓(False) 형태의 자료형
## mission>> 불린형의 True와 False를 출력하고 type() 함수를 활용하여 자료형을 주석으로 적기

'''print(True)
print(False)
print(type(True))
print(type(False))
'''

# [변수]
## 변수란?: 데이터를 저장할 공간. 할당연산자(=)를 활용.
## 특징: "언제든지 데이터를 변경"할 수 있다.
## 문법: 변수이름 = 데이터
## mission>> 라인하르트(or 내 게임 주 캐릭터)의 이름, 공격력, 공격속도, 최대거리(reach)를 변수로 저장하고 출력해보자.
## 라인하르트 정보: https://namu.wiki/w/%EB%9D%BC%EC%9D%B8%ED%95%98%EB%A5%B4%ED%8A%B8(%EC%98%A4%EB%B2%84%EC%9B%8C%EC%B9%98)#s-4.2

'''name='솔붕이'
dam='발당 19'
atsp='초당 9발'
re='55m'

print(name, dam, atsp, re)
print('우리 %s는 아직 안 죽었어!'%name)'''

# [연산]
## 연산이란?: 수나 식을 일정한 '규칙'에 따라 계산하는 것
## 대입연산: 할당연산자(=)를 활용하여 데이터를 변수에 대입하는 연산자
'''
ohgfriend = 13467
'''
## 숫자산술연산: + - * / 와 같은 수의 계산에 대한 연산자
## mission>> 7과 3에 대해서 + - * / // % **의 결과를 출력하기

'''
print(7+3)          #10
print(7-3)          #4
print(7*3)          #21
print(7/3)          #2.333335
print(7//3)         #2
print(7%3)          #1
print(7**3)         #345
'''

## 문자열연산: + *
## mission1>> 해시태그1,2,3를 변수로 받고 +연산을 사용하여 이를 한 문장으로 만들어 출력해보자
'''
tag1='#갓챠'
tag2='#이예ㅖㅖ'
tag=tag1+tag2
print(tag)
'''

## mission2>> *연산을 활용하여 같은 문장이 반복되는 문자열을 출력해보자
'''
string='정신나갈꺼같아'
print(string*10)
'''
## 복합할당연산자: 연산계의 줄임말
## mission>> 복함할당연산자를 활용하여 위에서 언급한 내 주 캐릭터의 스펙을 바꿔보자!
'''
attack=100
attack+=10      #attack=attack+10
print(attack)
attack-=10      #attack=attack-10
print(attack)
attack*=10      #attack=attack*10
print(attack)w
attack/=10      #attack=attack/10
print(attack)
attack//=10      #attack=attack//10
print(attack)
attack%=10      #attack=attack%10
print(attack)
attack**=10      #attack=attack**10
print(attack)
'''

