class Country:
    province_list2 = [2]
    pass
class Province:
    province_list = []
class Korea(Country, Province):
    pass
k = Korea()
print(k.province_list)
print(k.province_list2)
print(Korea.mro())