def generator1():
    print("yield 1 전")
    yield 1
    print("yield 2 전")
    yield 2
    print("yield 3 전")
    yield 3

def generator2():
    a = [10, 20, 30]
    for i in a:
        print('yield {} 전 출력'.format(i))
        yield i

def generator3():
    a = [10, 20, 30]
    yield from a

gen1 = generator1()
gen2 = generator2()
gen3 = generator3()
gen_list = list(gen3)
