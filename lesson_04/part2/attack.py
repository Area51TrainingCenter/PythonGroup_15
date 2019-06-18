class Human:
    def attack(self):
        print('Lanza una patada')


class Cyborg(Human):
    def attack(self):
        print('Lanza un láser')


class Ninja(Human):
    def attack(self):
        print('Lanza una estrella')


class A51(Ninja, Cyborg):
    pass


human = Human()
cyborg = Cyborg()
ninja = Ninja()
cyborg_ninja = A51()

human.attack()
cyborg.attack()
ninja.attack()
print()
cyborg_ninja.attack()
