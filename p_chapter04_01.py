# Chapter 04-01
# 시퀀스형

# 데이터 타입을 두가지로 나눔(컨테이너/플랫)
    # 컨테이너(Container : 서로다른 자료형[List, tuple, collections.deque])
        # a = [3, 3.0, 'a']
    # 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array, memoryview])

# 수정가능여부로 두가지로 나눔(가변/불변)
    # 가변(list, bytearray, array, memorybiew, deque)
    # 불변(tuple, str, bytes)
    
# 리스트 및 튜플 고급
# 지능형 리스트(Comprehending Lists)
chars = '+_)(*&^%$#@!)'
# chars[2] = 'h'  # ypeError: 'str' object does not support item assignment

code_list1 = []
for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))   # ord() : 해당 문자의 유니코드를 리턴
print(code_list1)   # [43, 95, 41, 40, 42, 38, 94, 37, 36, 35, 64, 33, 41]

# 지능형 리스트(Comprehending Lists) : for 문에서 append()함수 사용보다 속도가 빠름
code_list2 = [ord(s) for s in chars]
print(code_list2)


# 지능형 리스트(Comprehending Lists) + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))   # map(함수, 리스트) → 람다에 들어갈 변수 x로 사용됨
# 데이터 전처리시 많이 사용되는 filter함수
print(code_list3)

# 전체출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])     # chr() : ord()의 반대, 유니코드를 문자로 리턴
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

###### iterable 하다는 의미 #######
# print(dir(chars))   # __iter__가 dir 속성에 있으면, for문 사용이 가능하다 

# Generator 생성(Generator : 작은 메모리 사용으로도 연속되는 데이터를 만들어 낼수 있다.)
# Generator : 한번에 한개의 항목을 생성(메모리 유지x)
import array    # 플랫(하나의 자료형만 저장가능), 가변

list_chars = [ord(s) for s in chars]
print(list_chars)

tuple_g = (ord(s) for s in chars)  # list comprehending 에서 리스트를 튜플로 변경
print(tuple_g)  # <generator object <genexpr> at 0x7feb401a6ba0> : 값들을 튜플로 반환한 준비만 하고 있는 상태
print(type(tuple_g))    # <class 'generator'>
print(next(tuple_g))    # 첫번째인 43

array_g = array.array('I', (ord(s) for s in chars))
print(array_g)
print(type(array_g))    # <class 'array.array'>
print(array_g.tolist()) # tolist() : array를 리스트로 반환

print()
print()

# 제너레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))
# <generator object <genexpr> at 0x7fd2601a6ba0>
# 튜플로 감싸진 Comprehension 을 출력하면 제너레이터가 나옴
# 제너레이터 값을 확인하기 위해선 for문을 돌려서 하나씩 출력해야함
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)
    
    
# 리스트 주의사항 
# Shallow / Deep Copy

mark1 = [['~'] * 3 for _ in range(4)]   # 반복은 하는데 사용안할땐 명시적으로 _ 처리
mark2 = [['~'] * 3] * 4
print(mark1)    # 리스트 요소가 다 다른 id를 갖는다
print(mark2)    # 리스트 요소가 다 같은 id를 갖는다

# 수정할때 다른 결과를 보인다.
mark1[0][1] = 'X'
mark2[0][1] = 'X'
print(mark1)    # [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
print(mark2)    # [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']]

# 증명 1
print([id(i) for i in mark1])   # [140489858330688, 140489858310080, 140489858309888, 140489858309824] : id 다 다름
print([id(i) for i in mark2])   # [140489858309632, 140489858309632, 140489858309632, 140489858309632] : id 다 같음