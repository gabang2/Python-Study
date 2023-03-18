def abc(a, b, c):
    print(c, b, a)

print("-------------1")
abc(10, 20, 30)
print("-------------2")
abc(*[100, 200, 300])

def abcd(*args):
    print(args[0], args[1], args[2])

print("-------------3")
abcd(*[1000, 2000, 3000, 4000])

print("-------------4")
def air_line1(departure, arrival, flighttime):
    print("출발지는 : ", departure)
    print("도착지는 : ", arrival)
    print("비행 시간은 : ", flighttime)

myflight = {"departure": "서울", "arrival": "LA", "flighttime":"10시간"}
air_line1(**myflight)

print("-------------5")
def air_line2(**kwargs):
    print("출발지는 : ", kwargs['departure'])
    print("도착지는 : ", kwargs['arrival'])
    print("비행 시간은 : ", kwargs['flighttime'])

myflight = {"departure": "서울", "arrival": "LA", "flighttime":"10시간"}
air_line2(**myflight)

print("-------------6")
def air_line3(departure, **kwargs):
    print("출발지는 : ", departure)
    print("도착지는 : ", kwargs['arrival'])
    print("비행 시간은 : ", kwargs['flighttime'])

myflight = {"departure": "서울", "arrival": "LA", "flighttime":"10시간"}
air_line3(**myflight)


