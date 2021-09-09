class Car():    # 클래스 선언시 괄호() 있어도 되고 없어도 됨
    """ 
    Car class
    Author : Seo
    Date:2021.08.30
    """

    # 클래스 변수 : 모든 인스턴스가 공유함
    car_count = 0

    def __init__(self, company, details):       # 기본적으로 상속받는 인스턴스 메소드(매직/스페셜 메소드)
        self._company = company                 # 인스턴스 변수(_를 붙여주는 것이 개발자간의 약속)
        self._details = details
        Car.car_count += 1                      # __init__()함수가 호출될때마다 1씩증가 총생성된 인스턴스를 알아볼수 있음
    def __str__(self):                          # 기본적으로 상속받는 인스턴스 메소드(비공식적 사용자입장에서 사용)
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):                         # 기본적으로 상속받는 인스턴스 메소드(공식적 개발자입장에서 사용)
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):                       # 인스턴스 메소드 선언 : self를 사용하는 클래스내 함수
        print('Current ID :{}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

# self의 의미
car1 = Car('Ferrari', {'color':'white', 'horsepower':400, 'price':8000})    # car1 : 인스턴스 선언
car2 = Car('BMW', {'color':'Black', 'horsepower':270, 'price':5000})    # car2 : 인스턴스 선언
car3 = Car('Audi', {'color':'Silver', 'horsepower':300, 'price':6000})    # car3 : 인스턴스 선언

# 인스턴스 메소드에서는 self가 첫번째 매개변수로 넘어옴 : 인스턴스를 지칭할 예약어
print(id(car1)) # 32934592  각각 고유의 아이디
print(id(car2)) # 32934736
print(id(car3)) # 32934784
# 클래스는 같지만 각 인스턴스 들의 ID가 다름

print(car1._company == car2._company)   # 값을 비교 : False
print(car1 is car2) # 인스턴스 자체를 비교 : False

# dir & __dict__ 확인
print(dir(car1))    # 인스턴스가 갖고 있는 모든 어트리뷰트(클래스, 매직매소드 등)를 리스트로 보여줌
print(dir(car2))    # 상속받는 모든것을 보여준다

print(car1.__dict__)    # 인스턴스가 갖는 정보를 딕셔너리로 보여줌

# Doctring
print(Car.__doc__)  # 클래스 상세설명서를 호출함

# 실행
car1.detail_info()
Car.detail_info(car1)   # 이렇게 사용하려면 self가 선언되지 않았었기때문에 self에 car1을 전달해주어야
car2.detail_info()

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__))   # class의 ID는 동일하다

# 에러
# Car.detail_info()   # TypeError: detail_info() missing 1 required positional argument: 'self'
Car.detail_info(car1)   # 이렇게 사용하려면 self가 선언되지 않았었기때문에 self에 car1을 전달해주어야

print(car1.car_count)   # 3 : 인스턴스가 총 세개 생성되었으므로(car1, car2, car3 관계없이 공유하는 클래스 변수)
print(car2.car_count)   # 3 : 인스턴스가 총 세개 생성되었으므로(car1, car2, car3 관계없이 공유하는 클래스 변수)
print(car1.__dict__)    # 클래스 변수가 __dict__으로는 확인 안됨
print(dir(car1))        # 클래스 변수가 리스트에 나타남

# 접근
print(car1.car_count)   # 클래스 변수는 인스턴스로 접근해도 되고
print(Car.car_count)    # 클래스 변수는 클래스로 접근해도 됨 → 정석
# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 → 상위(클래스 변수, 부모클래스 변수))

del car2    # 인스턴스 삭제
# 삭제 확인
print(car1.car_count)  
print(Car.car_count)