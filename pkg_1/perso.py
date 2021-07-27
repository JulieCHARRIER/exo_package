class Perso:

    def __init__(self, name, level=1, exp=0):
        self.name = name
        self.level = level
        self.exp = exp


    def gain_level(self):
        self.level += 1
        print("Bravo, tu es enfin niveau {}!".format(self.level))
        self.exp = 0


    def gain_exp(self, exp):
        self.exp += exp
        if self.exp >= 100:
            self.gain_level()
