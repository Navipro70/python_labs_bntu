# __def_name__ - method (protected) in class, witch we not call,
# is call by itself when programs need (or when something happens with object)
# __init__ is constructor for initial params, __del__ - deconstructor

class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def __del__(self):
        print('Goodbye Mr.{0}'.format(self.name))

    @staticmethod
    def attack(another_warrior):
        another_warrior.health -= 20


sven = Warrior("sven")
pudge = Warrior("pudge")

while True:
    if pudge.health <= 0:
        print('Pudge dead')
        break
    elif sven.health <= 0:
        print('Sven dead')
        break
    hitter = input('Enter who you want hit: ')
    if hitter.upper().find(pudge.name.upper()):
        sven.attack(pudge)
    elif hitter.upper().find(sven.name.upper()):
        pudge.attack(sven)
    else:
        print('Incorrect name')
