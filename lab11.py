#           Corvinae
#           /     \
#        Corvus   Pica

class Birds:
    def __init__(self):
        self.doesFly = True
        # pass
    # doesFly = True

class Corvinae(Birds):
    eatsCarrion = True
    lifespan    = 30   # in years
    def sound(self):
        return 'Caw!'
    def layEgg(self):
        return 'Layed egg!'
    def sleep(self):
        return 'They sleep on trees!'
    def hunt(self):
        return 'Corvinae is also predators, which means they hunt for prey!'


class Corvus(Corvinae):
    color = 'Black'
    def sound(self):
        return 'Squak!'

class Pica(Corvinae):
    color = 'Gray'

Patty = Corvus()
Giby  = Pica()

print(Patty.eatsCarrion)
print(Patty.color)
print(Patty.lifespan)
print(Patty.sound())
print(Patty.doesFly)

print(Giby.color)
print(Giby.sound())
