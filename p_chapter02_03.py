class Car():    # 클래스 선언시 괄호() 있어도 되고 없어도 됨
    """ 
    Car class
    Author : Seo
    Date:2021.08.30
    Description : Class, Static, Instance Method
    """

    # 클래스 변수 : 모든 인스턴스가 공유함
    price_per_raise = 1.0   # 가격 상승률

    def __init__(self, company, details):       # 기본적으로 상속받는 인스턴스 메소드(매직/스페셜 메소드)
        self._company = company                 # 인스턴스 변수(_를 붙여주는 것이 개발자간의 약속)
        self._details = details
        # Car.car_count += 1                      # __init__()함수가 호출될때마다 1씩증가 총생성된 인스턴스를 알아볼수 있음
    def __str__(self):                          # 기본적으로 상속받는 인스턴스 메소드(비공식적 사용자입장에서 사용)
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):                         # 기본적으로 상속받는 인스턴스 메소드(공식적 개발자입장에서 사용)
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):                      # 인스턴스 메소드 선언 : self를 사용하는 클래스내 함수
        print('Current ID :{}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    def get_price(self):    # 현재가격
        return 'Before Car Price -> company: {}, price : {}'.format(self._company, self._details.get('price'))

    def get_price_calc(self):   # 상승가격
        return 'After Car Price -> company: {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method : 클래스 변수를 이용할때는 클래스 메소드를 이용하는것이 편리
    @classmethod    # 데코레이터
    def raise_price(cls, per):  # 클래스 메소드 선언 : Class를 사용하는 클래스내 함수(cls로 약속, self로 사용해도 가능은함)
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased.')

    # Static Method : (클래스/Self)인자 아무것도 받지 않음, 내가 정한 것만 받음
    @staticmethod   # 데코레이터
    def is_bmw(inst):
        if inst._company == 'BMW':
            return 'OK! This Car is {}'.format(inst._company)
        return 'Sorry, This car is not BMW'


# self의 의미
car1 = Car('Ferrari', {'color':'white', 'horsepower':400, 'price':8000})    # car1 : 인스턴스 선언
car2 = Car('BMW', {'color':'Black', 'horsepower':270, 'price':5000})    # car2 : 인스턴스 선언

# 전체정보
car1.detail_info()
car2.detail_info()

# 가격정보 : 직접접근(→ 좋은방법 아님)
print(car1._details.get('price'))
print(car2._details['price'])
# 가격정보 : 인스턴스 메소드로 접근(→ 좋은방법)
print(car1.get_price())
print(car2.get_price())

# 가격 인상 : 직접접근(→ 좋은방법 아님)
Car.price_per_raise = 1.4
print(car1.get_price_calc())
print(car2.get_price_calc())

# 가격 인상 : 클래스 메소드로 접근(→ 좋은방법 : 클래스 변수를 이용할때는 클래스 메소드 사용이 좋다)
Car.raise_price(1.6)    # 클래스메소드사용 :  클래스.클래스메소드(cls,)
print(car1.get_price_calc())    # 인스턴스메소드사용 : 인스턴스.인스턴스메소드(self,)
print(car2.get_price_calc())

# 인스턴스로 스테틱 메소드 호출
print(car1.is_bmw(car1))
print(car1.is_bmw(car2))
# 클래스로 스테틱 메소드 호출
print(Car.is_bmw(car1))
print(Car.is_bmw(car2)) 