# Höfundur: Ágúst Már Þórðarson
# Dagsetning: 03/11/26
# Verkefni: Einkunnir
# Athugasemdir:
# Gast þú leyst þetta verkefni án hjálpar? Já

student_grades = {
"Jón": 6,
"Anna": 9,
"Gunnar": 8,
"Siggi": 7,
"Erla": 4
}


def add_grade():
    baetaVidNemanda = input("Sláðu inn nafn nemanda: ")
    baetaVidEinkunn = int(input("Sláðu inn einkunn nemanda: "))
    student_grades[baetaVidNemanda] = baetaVidEinkunn


def update_grade():
    uppfaeraNemanda = input("Sláðu inn nafn nemanda sem þú vilt uppfæra: ")
    if uppfaeraNemanda in student_grades:
        uppfaeraEinkunn = int(input("Sláðu inn nýja einkunn: "))
        student_grades[uppfaeraNemanda] = uppfaeraEinkunn
    else:
        print(uppfaeraNemanda, "er ekki skráður. Endilega skráðu nemandann með aðgerð 1")


def get_grade():
    saekjaNemanda = input("Sláðu inn nafn nemanda sem þú vilt sækja einkunn fyrir: ")
    if saekjaNemanda in student_grades:
        print(saekjaNemanda, "er með einkunnina:", student_grades[saekjaNemanda])
    else:
        print(saekjaNemanda, "er ekki skráður. Endilega skráðu nemandann með aðgerð 1")

def calculate_average_grade():
    summa = 0
    for nafn in student_grades:


def print_dict():
    for nafn in student_grades:
        print(nafn, student_grades[nafn])



def main():
    adgerd = 1
    while adgerd != 0:
        print("Veldu aðgerð:")
        print("  1. Bæta við nemanda")
        print("  2. Uppfæra einkunn")
        print("  3. Sækja einkunn")
        print("  4. Reikna meðaltal einkunna")
        print("  5. Prenta út lista allra nemanda")
        print("  0. Loka forriti")
        adgerd = int(input("Sláðu inn númer aðgerðar: "))

        if adgerd == 1:
            add_grade()
        elif adgerd == 2:
            update_grade()
        elif adgerd == 3:
            get_grade()
        #elif adgerd == 4:
        #    calculate_average_grade()
        elif adgerd == 5:
            print_dict()

main()

    