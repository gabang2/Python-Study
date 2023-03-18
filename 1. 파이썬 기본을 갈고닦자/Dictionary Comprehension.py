from pprint import pprint as pp

"""
Key-Value순서 바꾸기, Key가 중복될 경우에는 마지막 것이 표시되는 것 주의하기
"""

country_capital = {"대한민국" : "서울",
                   "영국":"런던",
                   "포르투갈":"리스본",
                   "스페인":"마드리드"}

capital_country = {capital:country for country, capital in country_capital.items()}

print("*****나라 : 도시 출력하기*****")
pp(country_capital)

print("*****도시 : 나라 출력하기*****")
pp(capital_country)
