# Chapter06-03
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 → 단일 프로그램 안에서 여러일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 → 속도
# 코루틴(Coroutine)의 타입은 제너레이터

# 코루틴 : 단일(싱글) 쓰레드, 스택을 기반으로 동작하는 비동기 작업
# 쓰레드 : OS 관리, CPU 코어에서 실시간, 시분할 비동기 작업 → 멀티쓰레드
# yield/send()를 이용하여 : 메인루틴 <-> 서브 루틴
# 코루틴 제어, 상태, 양방향 전송

# 서브루틴 : 메인루틴에서 호출 → 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 → 동시성 프로그래밍(여러사람이 일하는것 같은)
# 코루틴 : 쓰레드에 비해 오버헤드 감소(운영체제에 무리 감소)
# 쓰레드 : 싱글쓰레드 → 멀티쓰레드 → 복잡 → 공유되는 자원 → 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생
# 파이썬 3.5 이상 : def → async,   yield → await로 사용가능(예약어)


# 코루틴 Ex1

def coroutine1():
    print('>>> coroutine started')
    i = yield   # yield키워드 들어가면 제너레이터(코루틴은 제너레이터에서 파생)
    print('>>> coroutine received : {}'.format(i))
    
# 메인 루틴
# 제너레이턴 선언
cr1 = coroutine1()  # 함수 호출

print(cr1, type(cr1))
# <generator object coroutine1 at 0x7fd20808f580> <class 'generator'>

# yield 지점까지 서브루틴 수행
# next(cr1)   # >>> coroutine started
# next(cr1)   # >>> coroutine received : None

# send() 함수 사용하지 않아서 아무것도 전달하지 않으면 None이 전달됨
# cr1.send(100)   # >>> coroutine received : 100
# send()라는 함수가 next()의 기능도 포함, 메인루틴에서 100을 주고 서브루틴에서 100을 받아서 i에 할당

# 잘못된 사용
# cr2 = coroutine1()
# next() 사용해서 yield에 멈춰있는 상태에서 send()로 값을 보내야한다.
# cr2.send(100)

# 코루틴 Ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNIG : 실행 상태
# GEN_SUSPENDED : Yield 대기 상태 → 이때 send() 사용
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x     # y를 메인루틴 → 서브루틴 전달, x를 서브루틴 → 메인루틴 전달
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))
    
cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))   # 제너레이터의 상태값 호출 → GEN_CREATED

print(next(cr3))    # >>> coroutine started : 10
                    # 10    x를 반환하고, y값을 받을 대기상태
print(getgeneratorstate(cr3))   # GEN_SUSPENDED

# cr3.send(100)       # y는 100을 받았고, z값을 받을 대기상태
print(cr3.send(100))    # >>> coroutine received : 100
                        # 110 x+y를 반환하고, z값을 받을 대기상태
                        
# 코루틴 Ex3
# StopIteration 자동 처리(파이썬 3.5이상 → await사용하면 처리가능)
# 중첩 코루틴 처리

def generator1():
    for x in 'AB':
        yield x     # A, B 리턴 받으려면 next() 두번 호출
    for y in range(1,4):
        yield y

t1 = generator1()

print(next(t1)) # A
print(next(t1)) # B
print(next(t1)) # 1
print(next(t1)) # 2
print(next(t1)) # 3
# print(next(t1)) # StopIteration

t2 = generator1()

print(list(t2)) # ['A', 'B', 1, 2, 3]


def generator2():
    yield from 'AB' # iterable한 데이터를 순차적으로 반환하겠다는 의미
    yield from range(1,4)
    
t3 = generator2()
print(next(t3)) # A
print(next(t3)) # B
print(next(t3)) # 1
print(next(t3)) # 2
print(next(t3)) # 3
# print(next(t3)) # StopIteration
