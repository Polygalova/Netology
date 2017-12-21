class animals:
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


class hoofed(animals):
    def __init__(self, name, age=0, size=4, is_hungry=False, tiredness=0, legs=4, tail=True):
        super().__init__(name, age, size, is_hungry, tiredness)
        self.legs = legs
        self.tail = tail


class birds(animals):
    def __init__(self, name, age=0, size=2, is_hungry=False, tiredness=0, legs=2, plumage=True):
        super().__init__(name, age, size, is_hungry, tiredness)
        self.legs = legs
        self.plumage = plumage


class cows(hoofed):
    pass


class goats(hoofed):
    pass


class sheeps(hoofed):
    pass


class pigs(hoofed):
    pass


class ducks(birds):
    pass


class chicken(birds):
    pass


class geese(birds):
    pass


Donald_duck = ducks('Donald')
Scrooge_McDuck = ducks('Scrooge', size=2)

Nif_nif = pigs('Nif_nif', age=1)
Naf_naf = pigs('Naf_naf', is_hungry=True)
Nuf_nuf = pigs('Nuf_nuf')

Donald_duck.get_hungry()
Nuf_nuf.get_tired(15)
Donald_duck.age = 3
Nuf_nuf.sleep(2)

print(Donald_duck.__dict__)
print(Scrooge_McDuck.__dict__)
print(Nif_nif.__dict__)
print(Naf_naf.__dict__)
print(Nuf_nuf.__dict__)
