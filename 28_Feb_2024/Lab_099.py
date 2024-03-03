# Hierarchical Inheritance

class Father:
    def home1(self):
        return "This is a Father"


class Pramod(Father):

    def home(self):
        return "This is a Pramod  Home"


class BroPramod(Father):
    def home(self):
        return "This is a brother home."


pramod = Pramod()
print(pramod.home())
print(pramod.home1())
