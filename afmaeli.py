# Höfundur: Ágúst Már Þórðarson
# Dagsetning: 03/11/26
# Verkefni: Afmæli uppfletti tala
# Athugasemdir:
# Gast þú leyst þetta verkefni án hjálpar? Já

gestir = {}

fjoldiGesta = int(input("Sláðu inn fjölda gesta sem ætla mæta í afmælið: "))
 
for i,j in enumerate(range(fjoldiGesta)):
    #vantar inn að splita fornafni frá eftirnafni
    nofnGesta = input("Sláðu inn nafn gests: ")
    gestir[nofnGesta] = i

hvadaGestur = input("Hvaða gest viltu athuga hvort mæti (q til að hætta): ")
while hvadaGestur != "q":
    if hvadaGestur in gestir:
        print("Já", hvadaGestur, "mætir")
        hvadaGestur = input("Hvaða gest viltu athuga hvort mæti (q til að hætta): ")
    else:
        print("Nei")
        hvadaGestur = input("Hvaða gest viltu athuga hvort mæti (q til að hætta): ")
