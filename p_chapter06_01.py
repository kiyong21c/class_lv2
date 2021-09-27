# Chapter06-01
# 병행성(concurrency)
# 이터레이터, 제네레이터
# Iterator(반복가능한 객체), Generator(이터레이터를 리턴하는 함수)

# 파이썬 반복 가능한 타입
# collections, text, list, Dict, Set, Tuple, unpacking, *args... : iterable

# 반복 가능한 이유? → iter() 함수 호출됨
t = 'ABCD'
print(dir(t))   # __iter__ 포함

for c in t:
    # print(c)
    pass
    
w = iter(t)

# print(next(w))  # A
# print(next(w))  # B
# print(next(w))  # C

# text를 for문을 이용했을떄 사용되는 메카니즘은 아래의 while문과 (사실은)같다
while True: # 종료 조건일 있을떄까지 반복되므로 조심해서 사용
    try:
        print(next(w))
    except StopIteration:   # StopIteration(더이상 next항목이 없으면 에러) 에러가 발생하면
        break
# ABCD

# 반복형 확인하는 방법
from collections import abc # abc: 추상클래스

print(dir(t))   #  dir()함수를 이용해서 들여다 볼수도 있으나 번거로움
print(hasattr(t, '__iter__'))   # True : t가 '__iter__'속성을 갖고있니?,
print(isinstance(t, abc.Iterable))  # True : t가 abc 추상클래스의 Iterable 인스턴스랑 같니? 

# next 패턴 : 클래스 활용 해보기
class WordSlpitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')
        
    def __next__(self):
        print('Called__next__') # __next__매직메서드가 사용되었는지 확인하기 위함
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration')
        self._idx += 1
        return word
    
    def __repr__(self):
        return 'WordSplit(%s)' %(self._text)
    
wi = WordSlpitter('Do today what you could do tommorrow')
print(wi)
print(next(wi)) # 클래스 이지만 인스턴스를 만들어 이터러블 하게 사용가능함
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))


# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 → 데이터양이 증가하면 메모리 사용 증가 → 제너레이터 사용 권장됨
# 2. 단위 실행 가능한 코루틴(corotine) 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self,text):
        self._text = text.split(' ')
    def __iter__(self):
        for word in self._text:
            yield word  # 제너레이터, 다음에 반환될 위치정보를 기억하고 있음
    def __repr__(self):
        return 'WordSplitGenerator(%s)' %(self._text)
    
    
wg = WordSplitGenerator('Do today what you could do tommorrow')

wt = iter(wg)

print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))

 