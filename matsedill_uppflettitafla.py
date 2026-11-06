# Höfundur: Ágúst Már Þórðarson
# Dagsetning: 06/11/26
# Verkefni: Uppflettitafla matseðill
# Athugasemdir:
# Gast þú leyst þetta verkefni án hjálpar? Já

ekkiTil = "Réttur ekki til á matseðli. Reyndu aftur"

menu = {
"Hamborgari": 1500,
"Pasta": 1390,
"Nautasteik": 3800,
"Lax": 1900,
"Salat": 1200,
"Pizza": 2800
}

def add_item(baetaVid, baetaVidVerd):

    if baetaVid in menu:
        print("Réttur nú þegar á matseðli. Reyndu aftur")
    else:
        menu[baetaVid] = baetaVidVerd
        print("Rétti",baetaVid, "bætt við")

def remove_item(remove):
    if remove in menu:
        menu.pop(remove)
        print(remove, "hefur verið fjarlægt að matseðli")
    else:
        print(ekkiTil)


def update_price(uppfaera, nyttVerd):

    if uppfaera in menu:
        menu[uppfaera] = nyttVerd
        print(uppfaera,"kostar nú:",nyttVerd)
    else:
        print(ekkiTil)


def get_price(hvadaRett):
    if hvadaRett in menu:
        print(hvadaRett, "kostar:", menu[hvadaRett])
    else:
        print(ekkiTil)



def take_order():
    pontunListi = []
    heildarVerd = 0
    panta = input("Hvað viltu panta? q til að hætta: ")

    while panta != "q":
        
        if panta not in menu:
            print(ekkiTil)
        else:
            pontunListi.append(panta)
            heildarVerd += menu[panta]

        panta = input("Hvað viltu panta? q til að hætta: ")

    print("Pöntunin þín: ")

    for i in pontunListi:
        print(i)
    print("Heildarverð:",heildarVerd)


def display_menu():
    for rettur,verd in menu.items():
        print(rettur, verd  )


def main():
    adgerd = 1
    while adgerd != 9:
        
        print("Veldu aðgerð: \n"
            "  1. Bæta við matseðilinn \n" \
            "  2. Fjarlæga rétt af matseðli \n" \
            "  3. Uppfæra verð á rétti \n" \
            "  4. Sækja verð rétts \n" \
            "  5. Panta \n" \
            "  6. Birta matseðil \n" \
            "  9. Loka forriti")

        adgerd = int(input("Veldu aðgerðarnúmer: "))

        if adgerd == 1:
            baetaVid = input("Hverju viltu bæta inn á matseðilinn?: ")
            baetaVidVerd = int(input("Hvað á það að kosta?: "))
            add_item(baetaVid, baetaVidVerd)

        elif adgerd == 2:
            fjarlaega = input("Hvað viltu láta fjarlæga af matseðli?: ")
            remove_item(fjarlaega)

        elif adgerd == 3:
            uppfaera = input("Hvað viltu láta uppfæra á matseðli?: ")
            nyttVerd = int(input("Hvað á nýja verðið að vera?: "))
            update_price(uppfaera, nyttVerd)

        elif adgerd == 4:
            hvadaRettur = input("Hvaða rétt viltu sækja verðið á?: ")
            get_price(hvadaRettur)

        elif adgerd == 5:
            take_order()

        elif adgerd == 6:
            display_menu()
main()

