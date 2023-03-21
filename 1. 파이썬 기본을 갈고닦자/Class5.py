'''덕 타이핑(duck typing)'''

class Parrot:
    def fly(self):
        print("Parrot flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

def lift_off(entity):
    entity.fly()

lift_off(Parrot())
lift_off(Airplane())
