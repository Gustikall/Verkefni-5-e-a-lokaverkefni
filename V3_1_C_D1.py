# Höfundur: Ágúst Már Þórðarson
# Dagsetning: 09/11/26
# Verkefni: Starfsmaður
# Athugasemdir:
# Gast þú leyst þetta verkefni án hjálpar? Já

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, email, salary, department, position):
        super().__init__(name, age)
        self.email = email
        self.salary = salary
        self.department = department
        self.position = position

    def Give_raise(self, p):
        nyttP = p/100
        launaHaekkun = nyttP * self.salary
        nyLaun = launaHaekkun + self.salary
        self.salary = nyLaun

    def Change_department(self, new_department):
        self.department = new_department
        return self.department

    def Promote(self, new_position):
        self.position = new_position
        return self.position

    def Add_overtime(self, hours):
        yfirVinna = hours * 5000
        nyLaun = yfirVinna + self.salary
        self.salary = nyLaun

    def __str__(self):
        return f"Nafn:{self.name}, Aldur: {self.age},Netfang: {self.email}, Laun: {self.salary}, Deild: {self.department}, Staða: {self.position}"

def main():
    employee1 = Employee("Jón Jónsson", 34, "jon@jon.is", 400000, "Söludeild", "Sölumaður")
    print(employee1.salary)
    employee1.Give_raise(10)
    print(employee1.salary)

    print(employee1.position)
    employee1.Promote("Sölustjóri")
    print(employee1.position)
    employee1.Change_department("Fjármálasvið")
    employee1.Promote("Fjármálastjóri")

    employee1.Add_overtime(12)
    print(employee1.salary)

    print(employee1)

main()