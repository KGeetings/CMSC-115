class Student:
    def __init__(self):
        self.firstName = "Default"
        self.lastNAme = "Studentname"
        self.studID = 0
        self.classList = []

    def __init__(self, fname, lname, studID):
        self.firstname = fname
        self.lastname = lname
        self.studID = studID



a = Student()
b = Student("Kenyon", "Geetings", "356")