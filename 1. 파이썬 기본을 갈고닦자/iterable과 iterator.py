""" iterator객체 만들기 """
a = [1, 2, 3]
iter1 = iter(a)
iter2 = a.__iter__()

""" iterator 객체 꺼내기 """
next(iter1)
for i in iter2:
	print(i)