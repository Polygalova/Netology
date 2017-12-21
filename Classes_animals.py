class Animals:
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


class Hoofed(Animals):
    def __init__(self, name, age=0, size=4, is_hungry=False, tiredness=0, legs=4, tail=True):
        super().__init__(name, age, size, is_hungry, tiredness)
        self.legs = legs
        self.tail = tail


class Birds(Animals):
    def __init__(self, name, age=0, size=2, is_hungry=False, tiredness=0, legs=2, plumage=True):
        super().__init__(name, age, size, is_hungry, tiredness)
        self.legs = legs
        self.plumage = plumage


class Cows(Hoofed):
    pass


class Goats(Hoofed):
    pass


class Sheep(Hoofed):
    pass


class Pigs(Hoofed):
    pass


class Ducks(Birds):
    pass


class Chicken(Birds):
    pass


class Geese(Birds):
    pass


Donald_duck = Ducks('Donald')
Scrooge_McDuck = Ducks('Scrooge', size=2)

Nif_nif = Pigs('Nif_nif', age=1)
Naf_naf = Pigs('Naf_naf', is_hungry=True)
Nuf_nuf = Pigs('Nuf_nuf')

Donald_duck.get_hungry()
Nuf_nuf.get_tired(15)
Donald_duck.age = 3
Naf_naf.eat()
Nuf_nuf.sleep(2)

print(Donald_duck.__dict__)
print(Scrooge_McDuck.__dict__)
print(Nif_nif.__dict__)
print(Naf_naf.__dict__)
#print(Nuf_nuf.__dict__)
