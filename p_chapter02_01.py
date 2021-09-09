# 객체지향 프로그래밍(OOP) → [코드의 자새용], [코드 중복 방지], [유지보수], [대형프로젝트]
# 규모가 큰 프로젝트(프로그램) → 함수 중심 → 데이터 방대 → 복잡
# 클래스 중심 → 데이터 중심 → 객체로 관리

# 일반적인 코딩(권장되지 않음, 관리 불편함)
# 차량1
car_company = 'Ferrari'
car_detail_1 = [{'color':'white'}, {'horsepower':400}, {'price':8000}]

# 차량2
car_company = 'BMW'
car_detail_2 = [{'color':'Black'}, {'horsepower':270}, {'price':5000}]

# 차량3
car_company = 'Audi'
car_detail_3 = [{'color':'Silver'}, {'horsepower':300}, {'price':6000}]


# 리스트 구조(관리하기가 불편, 인덱스 접근시 실수위험, 삭제 불편, 데이터 양이 많을시 인덱스파악 어려움)
car_company_list = ['Ferrari','Bmw','Audi']
car_detail_list = [
    {'color':'white'}, {'horsepower':400}, {'price':8000},
    {'color':'Black'}, {'horsepower':270}, {'price':5000},
    {'color':'Silver'}, {'horsepower':300}, {'price':6000}
]
del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()

# 딕셔너리 구조(코드반복 지속, 중첩문제(키 덮어쓸 가능성), 키 조회시 예외처리)

car_dicts = [
    {'car_company':'Ferrari', 'car_detail':{'color':'white', 'horsepower':400, 'price':8000}},
    {'car_company':'BMW', 'car_detail':{'color':'Black', 'horsepower':270, 'price':5000}},
    {'car_company':'Audi', 'car_detail':{'color':'Silver', 'horsepower':300, 'price':6000}}
]

del car_dicts[1]
print(car_dicts)

print()
print()

# 클래스 구조(구조설계 후 재사용성 증가, 코드반복 최소화, 다양한 메소드 활용)

class Car():    # 클래스 선언시 괄호() 있어도 되고 없어도 됨
    def __init__(self, company, details):        # 기본적으로 상속받는 인스턴스 메소드(매직/스페셜 메소드)
        self._company = company
        self._details = details

    def __str__(self):                          # 기본적으로 상속받는 인스턴스 메소드(비공식적 사용자입장에서 사용)
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):                         # 기본적으로 상속받는 인스턴스 메소드(공식적 개발자입장에서 사용)
        return 'repr : {} - {}'.format(self._company, self._details)


car1 = Car('Ferrari', {'color':'white', 'horsepower':400, 'price':8000})    # car1 : 인스턴스 선언
car2 = Car('BMW', {'color':'Black', 'horsepower':270, 'price':5000})    # car1 : 인스턴스 선언
car3 = Car('Audi', {'color':'Silver', 'horsepower':300, 'price':6000})    # car1 : 인스턴스 선언

print(car1)     # <__main__.Car object at 0x00C18A60> : 매직메소드
                # str : Ferrari - {'color': 'white', 'horsepower': 400, 'price': 8000} : __str__ 메소드 사용시
                # repr : Ferrari - {'color': 'white', 'horsepower': 400, 'price': 8000} : __repr__ 메소드 사용시
print(car2)
print(car3)

print(car1.__dict__)    # __dict__ : 속성정보, 클래스 안에 뭐가 들었는지 확인가능
print(car2.__dict__)   
print(car3.__dict__)   

print(dir(car1))        # dir() : 모든 메타정보를 보여줌
                        # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
                        #  '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
                        # '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
                        #  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_company', '_details']

# 리스트 선언
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

# 반복문(__str__ 호출됨)
for i in car_list:
    print(i) 