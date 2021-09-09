# Chapter 04-03
# 시퀀스형

# 데이터 타입을 두가지로 나눔(컨테이너/플랫)
    # 컨테이너(Container : 서로다른 자료형[List, tuple, collections.deque])
        # a = [3, 3.0, 'a']
    # 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array, memoryview])

# 수정가능여부로 두가지로 나눔(가변/불변)
    # 가변(list, bytearray, array, memorybiew, deque)
    # 불변(tuple, str, bytes)
    
# 해쉬테이블
# Key에 Value를 저장하는 구조, Key는 중복되면 안됨
# 파이썬 dictionary = 해쉬 테이블
# 키 값의 연산 결과(해쉬)에 따라 직접 접근이 가능한 구조
# Key 값을 해싱 함수를 통해서 해쉬 주소값을 얻고, 해쉬주소값을 기반으로 Key에 대한 value참조
# 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict → Key 중복 허용 x, Set → 중복 허용 x

# Dict 및 Set 심화

# Immutable Dict
from types import MappingProxyType  # 읽기전용 딕셔너리

d = {'key1':'value1'}

# Read Only
d_frozen = MappingProxyType(d)  # 읽기전용

print(d, id(d))                 # {'key1': 'value1'} 140586226359424
print(d_frozen, id(d_frozen))   # {'key1': 'value1'} 140586226343312


# 수정 불가
# d_frozen['key2'] = 'value2' # TypeError: 'mappingproxy' object does not support item assignment

# 수정 가능
d['key2'] = 'value2' # 해당 하는 키가 없을때는 추가됨
print(d)


s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'} # set() 함수를 사용하는것보다 직접 set에 넣는것이 속도측면에서 유리
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set()
# s4 = {} # <class 'dict'> : 비워놓으면 딕셔너리로 인식됨
s5 = frozenset(s1)  # 읽기전용 set

s1. add('Melon')
print(s1)

# s5.add('Melon') # AttributeError: 'frozenset' object has no attribute 'add'

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 지능형 집합(Comprehending Set)
from unicodedata import name
print({name(chr(i), '') for i in range(0, 256)})