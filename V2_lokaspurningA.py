# Höfundur: Ágúst Már Þórðarson
# Dagsetning: 08/11/26
# Verkefni: Lokaspurning útgáfa A
# Athugasemdir:
# Gast þú leyst þetta verkefni án hjálpar? Já

class OrderedPair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Set_element(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value

            
    def __add__(self,other):
        nyttX = self.x + other.x
        nyttY = self.y + other.y
        return OrderedPair(nyttX,nyttY)
    def __sub__(self,other):
        nyttX = self.x - other.x
        nyttY = self.y - other.y
        return OrderedPair(nyttX,nyttY)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ge__(self, other):
        par1 = self.x + self.y
        par2 = other.x + other.y

        if par1 >= par2:
            return True
        else:
            return False
    def __str__(self):
        return f"{self.x} {self.y}"

pair1 = OrderedPair(10,20)
pair2 = OrderedPair(20,10)

pairAdd = pair1 + pair2
pairSub = pair1 - pair2
pairEQ = pair1 == pair2

print(pairAdd)
print(pairSub)
print(pairEQ)
print(pair1 >= pair2, pair2 >= pair1)

pair1.Set_element(0,100)
print(pair1)
pair1.Set_element(1,100)
print(pair1)
