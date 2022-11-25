class Cat:
    '''Lớp Cat là lớp cơ sở'''
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed

    def eat(self):
        return 'meat'

    def vocalize(self):
        return 'Chuff'

    def __str__(self):
        st = "The "+type(self).__name__.lower()+' weighs '\
            + str(self.mass_in_kg) + ' kg, '\
            + "has a lifspan of " + str(self.lifespan_in_years)\
            + " years and can run at a maximum speed of "\
            + str(self.speed_in_kph) + " kqh."
        return st

    def print_cat(self):
        print("Infomation of", type(self).__name__.lower())
        print(self.__str__())
        print('The', type(self).__name__.lower(), 'eat', self.eat(), \
              "and has vocalization is", self.vocalize(), '.')

class Tiger(Cat):
    def __int__(self, mass=310, lifespan=26, speed=65):
        super().__init__(mass, lifespan, speed)
        self.coat_pattern = 'striped'

    def vocalize(self):
        return 'Roar'

    def swim(self):
        return 'Splash splash'

    def print_tiger(self):
        self.print_cat()
        print("The", type(self).__name__.lower(), \
              "and can swim with", self.swim(), '.')

class Liger(Tiger):
    '''Lớp Liger kế thừa lớp Tiger và có mở rộng'''
    def __init__(self, mass=190, lifespan=14, speed=80):
        super().__init__(mass, lifespan, speed)
        self.is_social = True

    def print_liger(self):
        self.print_tiger()
        print('And social custom of', \
              type(self).__name__.lower(), \
              'is', self.is_social, '.')

c = Cat(4, 18, 48)
c.print_cat()
t = Tiger(5, 18, 65)
t.print_tiger()
l = Liger(6, 24, 79)
l.print_liger()