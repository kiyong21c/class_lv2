# Chapter06-02
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 → 단일 프로그램 안에서 여러일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 → 속도

# Generator Ex1

def generator_ex1():
    print('Start')
    yield 'A Point' # 네이버에서 크롤링 후 '멈춰있기' 등으로 활용
    print('Continue')
    yield 'B Point' # next()가 호출되면 다음에서 크롤링 후 '멈춰 있기' 등으로 활용
    print('End')

temp = iter(generator_ex1())

# print(generator_ex1())  # generator : yield가 들어가면 generator가 된다
# print(temp) # generator

# print(next(temp))   #### temp는 iter()함수를 받은 변수이기 때문에 next()사용 가능
# Start
# A Point

# print(next(temp))
# Continue
# B Point

# print(next(temp))
# End
# StopIteration

for v in generator_ex1():   #### 제너레이터는 for문 등으로 호출
    # print(v)
    pass

# Generator Ex2

temp2 = [x * 3 for x in generator_ex1()]    # list      # yield 뒤부분이 x로서 return됨
temp3 = (x * 3 for x in generator_ex1())    # generator

print(temp2)    # ['A PointA PointA Point', 'B PointB PointB Point']
print(temp3)    # <generator object <genexpr> at 0x7ff3900ae740>

for i in temp2:     # list는 당연히 for 문으로 호출 가능
    print(i)        # 'Start', 'Continue', 'End'는 출력 안됨 : return받은 x만 temp2 리스트에 들어가 있기 때문

for i in temp3:     # generator는 for 문 등으로 호출
    print(i)        # 'Start', 'Continue', 'End' 출력됨 : return 받은 x의 위치 다음이 실행되기 때문
    
    
# Generator Ex3(중요 함수 : itertools 실습)

# count, takewhile, filterfalse, accumulate, chain, product, groupby

import itertools

gen1 = itertools.count(1, 2.5)  # 1부터 시작하고, 2.5씩 무한대 증가 : 1, 3.5, 6, ...

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한

# 조건
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))
for v in gen2:
    # print(v)
    pass

# 필터에 적용 안되는 조건의 값(필터 반대)
gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5]) # 1,2
for v in gen3:
    # print(v)
    pass

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1,101)])
for v in gen4:
    # print(v)
    pass
    
# 연결1
gen5 = itertools.chain('ABCDE', range(1,11,2))
print(gen5)         # <itertools.chain object at 0x7fa6e01c5b20>
print(list(gen5))   # ['A', 'B', 'C', 'D', 'E', 1, 3, 5, 7, 9]

# 연결2
gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))   # [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]

# 개별 
gen7 = itertools.product('ABCDE')
print(list(gen7))   # [('A',), ('B',), ('C',), ('D',), ('E',)]

# 개별-옵션(경우의수)
gen8 = itertools.product('ABCDE', repeat=2)
print(list(gen8))   # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'A'), ...]

# 그룹화
gen9 = itertools.groupby('AAABBCCCCCDDEEE')
# print(list(gen9))   # [('A', <itertools._grouper object at 0x7fdf081c59d0>), ('B', <itertools._grouper object at 0x7fdf081c59a0>), ...]
for chr, group in gen9:
    print(chr, ' : ', list(group))
'''
A  :  ['A', 'A', 'A']
B  :  ['B', 'B']
C  :  ['C', 'C', 'C', 'C', 'C']
D  :  ['D', 'D']
E  :  ['E', 'E', 'E']
'''
