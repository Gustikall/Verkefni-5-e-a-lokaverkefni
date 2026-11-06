# Höfundur: Ágúst Már Þórðarson
# Dagsetning: 05/11/26
# Verkefni: Afmæli - Value er listi
# Athugasemdir:
# Gast þú leyst þetta verkefni án hjálpar? Já

gestir = {}

fjoldiGesta = int(input("Sláðu inn fjölda gesta: "))

for i in range (fjoldiGesta):
    nafnGests = input("Sláðu inn nafn gests: ")
    x = nafnGests.split()
    gestir[i] = x


hvadaGestur = "x"
while hvadaGestur != "q":
    hvadaGestur = input("Hvaða gest áttu von á? q til að hætta: ")

    gestaListi = []

    for nafn in gestir:
        if hvadaGestur == gestir[nafn][0]:
            gestaListi.append(gestir[nafn])
        
    for i in gestaListi:
        x = i[0] + " " + i[1]
        print(x, "mætir")
        print(i)
        if hvadaGestur not in i[0]:
            print(hvadaGestur,"mætir ekki")