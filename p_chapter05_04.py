# # Chapter05-03
# 일급 함수(일급 객체)
# 클로저 기초
# 데코레이터(Decorator) : 사용하기는 쉬우나, 만들기는 어려움

# 장점
# 1. 중복제거, 코드간결, 공통함수 작성
# 2. 로깅, 프레임워크(플라스크,장고,텐서플로우), 유효성체크 → 공통 기능
# 3. 조합해서 사용 용이

# 단점
# 1. 가독성 저하
# 2. 특정 기능에 한정된 함수는 → 단일 함수로 작성하는 것이 유리
# 3. 디버깅 불편

# 데코레이터 실습
import time

def perf_clock(func):   # 함수를 인자로 받음
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 실행
        result = func(*args)    # 인자로 받은 함수가 여기서 동작
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ','.join(repr(arg)for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) → %r' %(et, name, arg_str, result))
        return result
    return perf_clocked # inner function을 리턴


# 데코레이터 사용
print('-' * 40, 'Called Decorator → time func')

@perf_clock
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)

time_func(1.5)  # 함수를 그냥 사용하기만 해도 데코레이터가 작동함

# 데코레이터 미사용 하고, 클로저 사용하듯이
none_deco1 = perf_clock(time_func)  # 변수 = 데코레이터함수(실행하고자하는 함수)
none_deco2 = perf_clock(sum_func)

print('-' * 40, 'Called None Decorator → time func')
none_deco1(1.5)                     # (변수였던)함수(실행하고자하는 함수에 들어갈 인자)
none_deco2(100, 200, 300, 400)