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


def add_grade(nem, eink):
    if nem in student_grades:
        print("Nemandi nú þegar á skrá, reyndu aftur")
    else:
        student_grades[nem] = eink
        return student_grades


def update_grade(nem, eink):
    if nem in student_grades:
        student_grades[nem] = eink
    else:
        print(nem, "er ekki skráður. Endilega skráðu nemandann með aðgerð 1")


def get_grade(nem):
    if nem in student_grades:
        print(nem, "er með einkunnina:", student_grades[nem])
    else:
        print(nem, "er ekki skráður. Endilega skráðu nemandann með aðgerð 1")

def calculate_average_grade():
    summa = 0
    for i,nafn in enumerate(student_grades, start=1):
        summa += student_grades[nafn]
    return(summa / i)




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
            baetaVidNemanda = input("Sláðu inn nafn nemanda: ")
            baetaVidEinkunn = int(input("Sláðu inn einkunn nemanda: "))
            add_grade(baetaVidNemanda, baetaVidEinkunn)

        elif adgerd == 2:
            uppfaeraNemanda = input("Sláðu inn nafn nemanda sem þú vilt uppfæra: ")
            uppfaeraEinkunn = int(input("Sláðu inn nýja einkunn: "))
            update_grade(uppfaeraNemanda, uppfaeraEinkunn)

        elif adgerd == 3:
            saekjaNemanda = input("Sláðu inn nafn nemanda sem þú vilt sækja einkunn fyrir: ")
            get_grade(saekjaNemanda)

        elif adgerd == 4:
            average = calculate_average_grade(student_grades)
            print(f"Meðaleinkunn allra nemanda: {average:.2f}")
        elif adgerd == 5:
            print_dict()

main()

    