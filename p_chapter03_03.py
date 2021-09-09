# Chapter03-03
# Special Method(Magic Method)
# 파이썬의 핵심 → 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스 안의 정의할수 있는 특정한(Built-in) 메소드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id,    type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt
from typing import NoReturn

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2) # 일반적인 방법

print(l_leng1)

# 네임드 튜플 (튜플인데 딕셔너리기능을 갖고있음)
from collections import namedtuple

# 네임드 튜플 선언(총 4가지 방법 있음)
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3)  # Point(x=1.0, y=5.0)
# print(pt3[0])   # 1.0 : 인덱스로도 접근가능
# print(pt3.x)    # 1.0 : 키값으로도 접근가능
print(pt4)

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2) # 네임드 튜플활용 방법

print(l_leng2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x','y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True)  # class 는 예약어
# 중복되는 키값으로는 네임드 튜플을 만들수 없는데 rename=True 로 해야가능

# 출력
print(Point1, Point2, Point3, Point4)   # <class '__main__.Point'>가 네번 나옴 : 클래스 타입

# Dict to Unpacking
temp_dict = {'x':75, 'y':55}    # DB 에서 딕셔너리로 넘겨준경우 네임드 튜플로 관리하기



# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40) # Point(x=10, y=20, _2=30, _3=40) x,y 말고는 rename이 허용됨
p5 = Point3(**temp_dict)    # 튜플은 *, 딕셔너리는 **  : Unpacking
print()

print(p1)
print(p2)
print(p3)
print(p4)   # rename test
print(p5)

# 사용
print(p1[0]+p2[1])  # 일반적인 방법
print(p1.x + p2.y)  # 네임드튜플의 키를 이용

# Unpacking
x, y = p3   # 튜플을 각각의 변수에 할당

print(x, y)

# 네임드 튜플의 메소드
temp = [52, 38]

# _make() : List를 NamedTuple로 만드는 함수
p1 = Point1._make(temp)
print(p1)   # Point(x=52, y=38)

# _filed : 필드 키값 확인
print(p1._fields, p2._fields)   # ('x', 'y') ('x', 'y')

# _asdict() : OrderdDict 반환(네임드 튜플을 딕셔너리로 변환)
print(p1._asdict())
print(p3._asdict())

# 실사용 실습
# 반 20명, 4개의 반(A, B, C, D)

# 네임드 튜플 선언
Classes = namedtuple('ClassesT', ['rank', 'number'])    # 네임드 튜플에 붙여지는 이름 : ClassesT

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]    # 연습해보자
ranks = 'A B C D'.split()   # 공백으로 잘라서 리스트에 담음

print(numbers)
print(ranks)

# 네임드 튜플 객체 생성
# List Comprehension
students1 = [Classes(rank, number) for rank in ranks for number in numbers] # 파이썬 문법의 강력함 한줄로 끝냄
print(students1)

###### 네임드 튜플은 데이터 모델링을 위해 사용됨 ######

# 추천
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
                for number in [str(n)
                    for n in range(1, 21)]]
print(students2)    # 리스트 반복문으로 만들때 한줄로 하는것보다 가독성이 크다.

# 출력
for s in students2:
    print(s)