from itertools import islice, count, chain

# islice - iterator 함수
secondary = islice((x for x in count() if x%2 == 0), 10)
print(type(secondary))

# chain - iterator 함수
country = ["대한민국", "스웨덴", "미국"]
city = ["서울", "스톡홀름", "워싱턴"]
c = chain(country, city)
for i in c:
    print(i)

# all - iterable 객체 함수
print(all([1, 2, 3]))
print(all([0, 2, 3]))

# any - iterable객체 함수
print(any([0, 2, 3]))
print(any([False, [], 0]))

# zip - iterable객체 함수
a = zip([1, 2, 3], (4, 5, 6))
print(next(a))
for coun, cap in zip(country, city):
    print("국가명: {}, 수도: {}".format(coun, cap))