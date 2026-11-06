# Höfundur: Ágúst Már Þórðarson
# Dagsetning: 06/11/26
# Verkefni: Sameiginlegar plötur
# Athugasemdir:
# Gast þú leyst þetta verkefni án hjálpar? Já

fjoldiDiska = input("Sláðu inn fjöldi diska sem þið kæró eigið. F: X X: ")

splitDiskar = fjoldiDiska.split()
tala1 = int(splitDiskar[0])
tala2 = int(splitDiskar[1])

set1 = set()
set2 = set()

for i in range(tala1):
    x = int(input("Nr. plötu hjá fyrri aðila: "))
    set1.add(x)

for j in range(tala2):
    x = int(input("Nr. plötu hjá seinni aðila: "))
    set2.add(x)

print("Fjöldi platna sem báðir aðila eiga", len(set1 & set2))

