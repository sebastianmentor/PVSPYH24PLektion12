class Student:
    def __init__(self, förnamn, efternamn):
        self.förnamn = förnamn
        self.efternamn = efternamn

class Larare:
    def __init__(self, namn):
        self.namn = namn

    def undervisa(self, student):
        print(f"{self.namn} undervisar {student.namn}")

# Skapa objekt
larare = Larare("Karin")
student = Student("Anna", "Cramling")

# Använda associering
larare.undervisa(student)


class Läkare:
    def __init__(self, namn):
        self.namn = namn

    def behandla_patient(self, patient):
        print(f"{self.namn} behandlar {patient.namn}")

class Patient:
    def __init__(self, namn):
        self.namn = namn

# Skapa instanser
läkare = Läkare("Dr. Karlsson")
patient = Patient("Anna Andersson")

# Läkare interagerar med patient
läkare.behandla_patient(patient)
