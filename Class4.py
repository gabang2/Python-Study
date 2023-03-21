'''추상 클래스'''
from abc import *

class AbstractCountry(metaclass=ABCMeta):
    name = "국가명"
    capital = "수도"

    def show(self):
        print('국가 클래스의 메소드입니다.')

    @abstractmethod
    def show_capital(self):
        print('국가의 수도는?')

class Korea(AbstractCountry):
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital
    
    def show_name(self):
        print('국가의 이름은 : ', self.name)

    def show_capital(self):
        super().show_capital()
        print(self.capital)