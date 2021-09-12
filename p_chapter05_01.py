# Chapter05-01
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)

# 5! = 5 * 4 * 3 * 2 * 1

# 함수 객체

def factorial(n):
    '''Factorial Function -> n : int'''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1)   # 재귀함수 : 함수내에서 함수 호출

class A:
    pass

print(factorial(5)) # 120
print(factorial.__doc__)
print(type(factorial), type(A)) # <class 'function'> <class 'type'>
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))    # 교집합을 빼다.
# {'__annotations__', '__kwdefaults__', '__defaults__', '__globals__', '__closure__', '__get__', '__qualname__', '__name__', '__code__', '__call__'}
print(factorial.__name__)   # factorial
print(factorial.__code__)   # <code object factorial at 0x7fdee815b870, file "/Users/kiyongseo/Documents/Python_Programming/python_ex/p_chapter05_01.py", line 12>
# 함수는 객체 취급

##### 변수에 할당 #####
# var_func = factorial(5) # 이건 함수를 실행하여 나온결과를 변수에 할당
var_func = factorial   # 함수 자체를 변수에 할당

print(var_func) # <function factorial at 0x7fa6980e6f70>
print(var_func(5))  # 실행 됨 : 변수에 할당 가능
print(map(var_func, range(1,6)))    # <map object at 0x7fa8280f7f70>
print(list(map(var_func, range(1,6))))  # [1, 2, 6, 24, 120]


##### 함수 인수 전달 및 함수로 결과 반환 → 고위함수(Higher-order function) #####
# map, filter, reduce
print(list(map(var_func, filter(lambda x: x % 2, range(1,6))))) # 함수를 map함수의 인자로 전달,
print([var_func(i) for i in range(1, 6) if i % 2])  # if i % 2 : i를 2로 나누어서 나머지가 '있을' 경우만(홀수만)

# reduce
from functools import reduce    # 파이썬 버전업 되면서 reduce함수는 밖으로 빠짐
from operator import add
print(reduce(add, range(1, 11)))
print(sum(range(1, 11)))    # 이게더 편하긴함

# 익명함수(lambda)
# 가급적 주석 작성 : 타인의 가독성이 따라짐
# 가급적 일반함수를 사용하도록 권장됨
print(reduce(lambda x, t: x+t, range(1,11)))    # reduce 누적해서 연산함

# callable : 호출 연산자 → 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인(__call__ 있으면 가능함)
print(callable(str), callable(A), callable(list), callable(var_func), callable(factorial), callable(3.14))
# True True True True True False : 3.14(3) → 이런식으로 호출 불가능
# 3.14(3) # TypeError: 'float' object is not callable

# partial 사용법 : 인수 고정 → 콜백 함수 사용
from operator import mul
from functools import partial
print(mul(10,11))
# partial : 인수 고정
five = partial(mul, 5)  # mul 함수를 인수로 전달, partial 함수를 변수에 할당, mul 함수는 인수를 두개 받는데 5밖에 없다, 5 * ?
# 5는 고정하고 곱할값을 인수로 five 함수(변수였던) 의 인수로 받는다.

# 고정 추가
six = partial(five, 6)

print(five(10)) # 5 * 10
print(five(100)) # 5 * 100
print(six())
print(five(i) for i in range(1,11)) # <generator object <genexpr> at 0x7fd7701d97b0>
print([five(i) for i in range(1,11)])   # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(list(map(five, range(1,11))))