class Perso:

    def __init__(self, name, level=1, exp=0,seuil_exp=100):
        self.name = name
        self.level = level
        self.exp = exp
        self.seuil_exp = seuil_exp


    def gain_level(self):
        self.level += 1
        print("Bravo, tu es enfin niveau {}!".format(self.level))



    def gain_exp(self, exp):
        self.exp += exp
        if self.exp >= self.seuil_exp:
            self.gain_level()
            self.exp -= self.seuil_exp
            self.seuil_exp += 20
