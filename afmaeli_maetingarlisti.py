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
    maeting = ""
    hvadaGestur = input("Hvaða gest áttu von á? q til að hætta: ")

    gestaListi = []

    for nafn in gestir:
        if hvadaGestur == gestir[nafn][0] and len(gestir[nafn]) == 2:
            gestaListi.append(gestir[nafn])
        
    for i in gestaListi:
        x = i[0] + " " + i[1]
        maeting += x + ", "
    if len(gestaListi) > 1:
        print("Gestir með fornafnið", hvadaGestur,":", maeting)
    else:
        print("Enginn gestur að nafni",hvadaGestur)


