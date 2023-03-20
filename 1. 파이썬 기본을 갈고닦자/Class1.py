class Flight:
    def __init__(self, number): # 객체 속성 초기화 역할
        if not number > 0:
            raise ValueError("0보다 큰 숫자를 사용해야 합니다.")
        self.__number = number

    def number(self):
        return self.__number
    
class CountryName:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("이름 : ", self.name)

    def show(self, abc):
        print("abc: ", abc)