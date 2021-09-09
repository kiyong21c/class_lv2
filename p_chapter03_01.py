# Chapter03-01
# Special Method(Magic Method)
# 파이썬의 핵심 → 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스 안의 정의할수 있는 특정한(Built-in) 메소드

# 기본형
print(int)  # <class 'int'>

# 모든 속성 및 메소드 출력
print(dir(int))

n = 10

print(type(n)) # <class 'int'>

# 흔히사용하는 int도 클래스이며, 매직메소드를 이용하여 간편하게 사용되도록한다.
print(n + 100)
print(n.__add__(100))   # __add__ 매직메소드를 이용하여 +를 사용
print(n.__doc__)
print(n.__bool__())
print(n * 100, n.__mul__(100))

# 클래스 예제
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price
        
    def __str__(self):  # 일반적인 print() 사용시 return됨
        return 'Fruit Class Info : {} {}'.format(self._name, self._price)
    
    def __add__(self, x):
        print('called __add__')
        return self._price + x._price
    
    def __sub__(self, x):
        print('called __sub__')
        return self._price - x._price
    
    def __le__(self, x):  # 크기비교(<=)
        print('called __le__')
        if self._price <= x._price:
            return True
        else:
            return False
    
    def __ge__(self, x):  # 크기비교(>=)
        print('called __ge__')
        if self._price >= x._price:
            return True
        else:
            return False

# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# 일반적인 방법
# print(s1._price + s2._price)    # 가독성, 효율성 떨어지는 방법

# 매직메소드 활용
print(s1 + s2)  # +를 사용할때 __add__ 매직메소드가 호출됨, self는 s1이 되고, x는 s2가 됨
print(s1 - s2)  # -를 사용할때 __sub__ 매직메소드가 호출됨, self는 s1이 되고, x는 s2가 됨
print(s1 >= s2)
print(s1 <= s2)
print(s1)
print(s2)
