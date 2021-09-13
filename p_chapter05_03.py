# Chapter05-03
# 일급 함수(일급 객체)
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 → 후에 접근(엑세스) 가능하도록 도와줌

# Closure 사용
def closure_ex1():
    # Free variable(자유변수) : 내가 사용하려는 함수 바깥에서 선언된 변수, 값이 보존되어있음
    # 클로저 영역
    series = [] # 함수의 호출이 끝나도 series 는 보존되어있음
    def averager(v):
        series.append(v)
        print('inner>>>{}/{}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager     # 함수(자체O, 결과X)를 반환(return) 가능

avg_closure1 = closure_ex1()
print(avg_closure1) # <function closure_ex1.<locals>.averager at 0x7fbf90188c10> : local의 averager 함수
print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()
print()

# function inspection
print(dir(avg_closure1))    # '__call__', '__closure__',...
print(dir(avg_closure1.__code__))   # 'co_freevars',... : 자유변수
print(avg_closure1.__code__.co_freevars)    # 자유변수 확인해보자 → 'series'
print(avg_closure1.__closure__[0].cell_contents)    # [10, 30, 50]

# 잘못된 클로저 사용 예
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0
    def averager(v):
        cnt += 1    # UnboundLocalError: local variable 'cnt' referenced before assignment
        total += v
        return total / cnt
    return averager
avg_closure2 = closure_ex2()
print(avg_closure2(10))

# 잘못된 클로저 사용 예 → 수정
def closure_ex3():
    # Free variable
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return averager
avg_closure3 = closure_ex3()
print(avg_closure3(10))
print(avg_closure3(20))
print(avg_closure3(30))