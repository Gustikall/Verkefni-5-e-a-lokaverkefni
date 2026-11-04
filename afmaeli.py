# Höfundur: Ágúst Már Þórðarson
# Dagsetning: 04/11/26
# Verkefni: Afmæli uppflettitala
# Athugasemdir:
# Gast þú leyst þetta verkefni án hjálpar? Já

gestir = {}

fjoldiGesta = int(input("Sláðu inn fjölda gesta: "))

for i in range (fjoldiGesta):
    nafnGests = input("Sláðu inn nafn gests: ")
    gestir[nafnGests] = i
print(gestir)

hvadaGestur = input("Hvaða gest áttu von á? q til að hætta: ")
while hvadaGestur != "q":

    if hvadaGestur in gestir:
        print(hvadaGestur, "mætir")
    else:

        for nafn in gestir:
            splitNafn = nafn.split()
            if hvadaGestur == splitNafn[0] and len(splitNafn) == 2:
                print("Nei en,", splitNafn[0], splitNafn[1], "mætir")
                break
            else:
                print("Nei")
    hvadaGestur = input("Hvaða gest áttu von á? q til að hætta: ")