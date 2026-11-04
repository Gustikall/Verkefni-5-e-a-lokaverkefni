# Höfundur: Ágúst Már Þórðarson
# Dagsetning: 04/11/26
# Verkefni: Afmæli - Value er listi
# Athugasemdir:
# Gast þú leyst þetta verkefni án hjálpar? Já

gestir = {}

fjoldiGesta = int(input("Sláðu inn fjölda gesta: "))

for i in range (fjoldiGesta):
    nafnGests = input("Sláðu inn nafn gests: ")
    gestir[i] = [nafnGests]
print(gestir)


hvadaGestur = input("Hvaða gest áttu von á? q til að hætta: ")

for nafn in gestir:
    x = gestir[nafn]
    print(x.split())
