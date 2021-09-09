
# Chapter 04-02
# 시퀀스형

# 데이터 타입을 두가지로 나눔(컨테이너/플랫)
    # 컨테이너(Container : 서로다른 자료형[List, tuple, collections.deque])
        # a = [3, 3.0, 'a']
    # 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array, memoryview])

# 수정가능여부로 두가지로 나눔(가변/불변)
    # 가변(list, bytearray, array, memorybiew, deque)
    # 불변(tuple, str, bytes)
    
# 리스트 및 튜플 고급
# Unpacking

# b, a = a, b 

print(divmod(100, 9))   # 100/9 의 몫과 나머지 튜플로 반환 : (11, 1)
print(*(divmod(100, 9)))    # 100/9 의 몫과 나머지를 풀어서 반환 : 11, 1
print(divmod(*(100, 9)))    # 튜플로 값을 넣을땐 *로 풀어준다
# print(divmod((100, 9)))    # 튜플로 묶여있어서 하나의 값으로 인식

# x, y, rest = range(10)
# ValueError: too many values to unpack (expected 3)
x, y, *rest = range(10)
print(x, y, rest)   # 0 1 [2, 3, 4, 5, 6, 7, 8, 9]
x, y, *rest = range(2)
print(x, y, rest)   # 0 1 []

# Mutable(가변형) vs Immutable(불변형)

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(l, id(l))
print(m, id(m))

l *= 2
m *= 2

print(l, id(l))
print(m, id(m)) # 리스트는 동일한 id에 변수가 재할당됨

# sort vs sorted
# reverse, key=len, key=str.Lower, key=func...

# sorted : 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted-', sorted(f_list))
print('sorted-', sorted(f_list, reverse=True))  # reverse 기본값은 False
print('sorted-', sorted(f_list, key=len))  # 글자 길이 순으로 정렬
print('sorted-', sorted(f_list, key=lambda x: x[-1]))  # 마지막 글자 기준으로 정렬
print('original', f_list)

# sort : 정렬 후 객체 직접 변경(원본이 변경됨)
print('sort-', f_list.sort(), f_list)   # f_list.sort() 반환값 None
print('sort-', f_list.sort(reverse=True), f_list)   # f_list.sort() 반환값 None
print('sort-', f_list.sort(key=len), f_list)   # f_list.sort() 반환값 None
print('sort-', f_list.sort(key=lambda x: x[-1]), f_list)   # f_list.sort() 반환값 None

# List vs Array 적합한 사용법
# 1. List 기반 : 융통성, 다양한 자료형, 범용적 사용
# 2. Array 기반 : 숫자 위주, 배열(리스트와 거의 호환됨)