# Chapter05-02
# 일급 함수(일급 객체)
# 클로저 기초

# 파이썬 변수 범위(Scope)

# Ex1
def func_v1(a):
    print(a)
    print(b)
    
# func_v1(10) # NameError: name 'b' is not defined

# Ex2
b = 20
def func_v2(a):
    print(a)
    print(b)

func_v2(10)

# Ex3-1
c = 30
def func_v3(a):
    print(a)
    print(c)    # UnboundLocalError: local variable 'c' referenced before assignment
    c = 40
# func_v3(10)

# Ex3-2
c = 30
def func_v3(a):
    c = 40  
    print(a)
    print(c)    # local variable 'c' 참조
print('>>',c)   # global variable 'c' 참조
func_v3(10)

# Ex3-3
c = 30
def func_v3(a):
    global c    ## 함수내에 global 사용하는것은 추천되는 코딩은 아님
    print(a)
    print(c)    # local variable 'c' 참조
    c = 40  
print('>>', c)   # global variable 'c' 참조
func_v3(10)
print('>>>', c) # global 선언된 'c' 가 참조

# Closure(클로저) 사용 이유
# 서버 프로그래밍 → 동시성(concurrency) 제어 → 같은 메모리 공간에 여러 자원이 접근 → 교착상태(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 → Erlang
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 구조를 적극적으로 사용 → 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom,STM → 멀티스레드(Coroutine) 프로그래밍에 강점
# 함수가 끝났어도 함수 내부의 상태를 기억한다

a = 100

print(a + 100)
print(a + 1000)

# 결과 누적(함수 사용)
print(sum(range(1,51))) # sum 함수

# 클래스 이용
class Averager():
    def __init__(self):
        self._series = []
        
    def __call__(self, v):  # __call__ 매직메소드가 있으면 callable하다 : class를 함수처럼 호출할 수 있음
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
averager_cls = Averager()

# 누적
print(averager_cls(10)) # 클래스를 함수처럼 실행
print(averager_cls(30)) # 클래스를 함수처럼 실행
print(averager_cls(50)) # 클래스를 함수처럼 실행
# 클래스가 실행되고 난 이후에 .series의 리스트 안에 기억되고 있음 : 클로저의 개념