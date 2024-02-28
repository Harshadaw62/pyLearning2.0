# Single Inheritance
# Multi Level

class GF:

    name = "Pramod"

    def home(self):
        self.name2 = "Pramod"
        print("5BHK")


class Father(GF):
    def home2(self):
        print("GOA")


class Son(Father):
    def home3(self):
        print("Bangalore")


pramod = Son()
pramod.home()
pramod.home2()
pramod.home3()
print("---------")
mmd = Father()
mmd.home()
mmd.home2()
print("---------")
gkd = GF()
gkd.home()