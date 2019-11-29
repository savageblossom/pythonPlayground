# import random
#
# class Robot:
#     def __init__(self, name):
#         self.name = name
#         self.hp = random.random()
#     def sayHi(self):
#         print('Hi, I am ' + self.name)
#     def needsDoctor(self):
#         if self.hp < 0.8:
#             return True
#         else:
#             return False
#
# class PhysicianRobot(Robot):
#     def sayHi(self):
#         print('Everything will be okay!')
#         print(self.name + " takes care of you!")
#     def heal(self, robo):
#         robo.hp = random.uniform(robo.hp, 1)
#         print(robo.name + " has been healed by " + self.name + "!")
# doc = PhysicianRobot("The Doctor")
# rob_list = []
# for i in range(5):
#     x = Robot("Marvin" + str(i))
#     if x.needsDoctor():
#         print('hp of ' + x.name + ' before healing: ', x.hp)
#         doc.heal(x)
#         print('hp of ' + x.name + ' after healing: ', x.hp)
#         rob_list.append((x.name, x.hp))
#
# print(rob_list)

class B:
    __count = 0
    def __init__(self):
        B.__count += 1

    def pObject(self):
        return self.__count
a = B()

print(a.pObject())
