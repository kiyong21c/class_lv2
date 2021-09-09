# Chapter03-02
# Special Method(Magic Method)
# 파이썬의 핵심 → 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스 안의 정의할수 있는 특정한(Built-in) 메소드

# 클래스 예제2(벡터)
# (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50,15)
# Max(5,10) = 10

class Vector(object):   # object 안써도됨
    def __init__(self, *args):   # packing
        '''
        Create a vector, example : v = Vector(5, 10)
        '''
        if len(args) == 0:   # v = Vector()  라고 인스턴스 생성했다면
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args
    
    def __repr__(self):
        '''
        Return the vector informations.
        '''
        return 'Vector(%r, %r)' % (self._x, self._y)
    
    def __add__(self, other):
        '''
        Return the vector add of self and other
        '''
        return Vector(self._x + other._x, self._y + other._y)
        
    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self): # (0,0)인지 확인
        return bool(max(self._x, self._y))  # 둘중 큰값이 0인지 확인(0이라면 False)

# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

# 매직 메소드 출력
print(Vector.__init__.__doc__)  # '''설명서'''가 메소드 단위안에 들어있으므로
print(Vector.__repr__.__doc__) 
print(Vector.__add__.__doc__)  
print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2))
print(bool(v3))
