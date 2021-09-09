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

# Dict 구조
print(__builtins__.__dict__)

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = [10, 20, [30, 40, 50]]

print(hash(t1)) # 465510690262297113 : hash함수를 사용할 수 있는것은 불변형일떄만
# print(hash(t2)) # TypeError: unhashable type: 'list'

# Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))   # 튜플안에 튜플 → 딕셔너리로 전환

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:  # key가 중복되면
        new_dict1[k].append(v)  # 중복되는 key의 value를 value리스트에 추가 
    else:
        new_dict1[k] = [v]
print(new_dict1)    # {'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
print(new_dict2)    # {'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}

# 주의 사항
new_dict3 = {k : v for k, v in source}  # 키 중복시 처리가 안되어 나중 키값으로 덮어쓰게됨
print(new_dict3)    # {'k1': 'val2', 'k2': 'val5'}