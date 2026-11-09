# Höfundur: Ágúst Már Þórðarson
# Dagsetning: 08/11/26
# Verkefni: Lokaspurning útgáfa B
# Athugasemdir:
# Gast þú leyst þetta verkefni án hjálpar? Já


class Fraction:
    def __init__(self, t, n=1):
        self.t = t
        self.n = n

    def Inverse(self):
        nyttT = self.n
        nyttN = self.t
        return Fraction(nyttT,nyttN)

    def __add__(self, other):
        nyrN = self.n * other.n
        nyrT1 = self.t * other.n
        nyrT2 = other.t * self.n
        nyrT = nyrT1 + nyrT2
        return Fraction(nyrT,nyrN)

    def __sub__(self, other):
        nyVHT = self.t * other.n
        nyHHT = other.t * self.n
        nyrN = self.n * other.n
        nyrT = nyVHT - nyHHT
        return Fraction(nyrT,nyrN)

    def __float__(self):
        floaterAlert = self.t / self.n
        return floaterAlert

    def __str__(self):
        return f"{self.t}/{self.n}"

a = Fraction(3,4)
b = Fraction(1,2)

print(a + b)
print(a - b)
print(a.Inverse())
print(float(a))
print(a)


class Soldier:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Soldier {self.name} reporting for duty!")

class Sniper(Soldier):
    def shoot(self):
        print(f"{self.name} has fired!")

class Medic(Soldier):
    def heal(self,other):
        print(f"{self.name} has healed {other.name}!")
    def introduce(self):
        print(f"Medic {self.name} has arrived!")

medic = Medic("Gústi")
wounded = Soldier("Arnar")

medic.heal(wounded)
medic.introduce()

        