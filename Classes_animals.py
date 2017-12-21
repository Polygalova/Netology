class AnimalsClass:
    def __init__(self, name, age=0, size=4, is_hungry=False, tiredness=0):
        self.name = name
        self.age = age
        self.size = size
        self.is_hungry = is_hungry
        self.tiredness = tiredness

    def get_hungry(self):
        self.is_hungry = True

    def eat(self):
        self.is_hungry = False

    def get_tired(self, hours):
        self.tiredness += hours

    def sleep(self, hours_to_sleep):
        delta_tiredness = int(4 * hours_to_sleep / self.size)
        if self.tiredness > delta_tiredness:
            self.tiredness -= delta_tiredness
        else:
            self.tiredness = 0


class HoofedClass(AnimalsClass):
    def __init__(self, name, age=0, size=4, is_hungry=False, tiredness=0, legs=4, tail=True):
        super().__init__(name, age, size, is_hungry, tiredness)
        self.legs = legs
        self.tail = tail


class BirdsClass(AnimalsClass):
    def __init__(self, name, age=0, size=2, is_hungry=False, tiredness=0, legs=2, plumage=True):
        super().__init__(name, age, size, is_hungry, tiredness)
        self.legs = legs
        self.plumage = plumage


class CowsClass(HoofedClass):
    pass


class GoatsClass(HoofedClass):
    pass


class SheepClass(HoofedClass):
    pass


class PigsClass(HoofedClass):
    pass


class DucksClass(BirdsClass):
    pass


class ChickenClass(BirdsClass):
    pass


class GeeseClass(BirdsClass):
    pass


Donald_duck = DucksClass('Donald')
Scrooge_McDuck = DucksClass('Scrooge', size=2)

Nif_nif = PigsClass('Nif_nif', age=1)
Naf_naf = PigsClass('Naf_naf', is_hungry=True)
Nuf_nuf = PigsClass('Nuf_nuf')

Donald_duck.get_hungry()
Nuf_nuf.get_tired(15)
Donald_duck.age = 3
Naf_naf.eat()
Nuf_nuf.sleep(2)

print(Donald_duck.__dict__)
print(Scrooge_McDuck.__dict__)
print(Nif_nif.__dict__)
print(Naf_naf.__dict__)
print(Nuf_nuf.__dict__)
