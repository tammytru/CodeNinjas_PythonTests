#----- CLASS SCHEDULER (HARD) -----#

class Student:
    def __init__(self, n):
        self.name = n
        self.grades = []
        self.sched = []
    
    def add_class(self, clas, gr):
        self.sched.append(clas)
        self.grades.append(gr)
    
    def drop_class(self, i):
        del self.sched[i]
        del self.grades[i]

    def print_sched(self):
        print("Student:", self.name)
        for i in range(0, len(self.sched)):
            print(i+1, ":", self.sched[i], "Grade: ", self.grades[i])

#def print_student()

students = []

while True:
    print("1. Add new student")
    print("2. Update schedule")
    print("3. Drop class")
    print("4. Print schedule")
    print("5. Remove student")
    option = input("Choose an option: ")

    if option == 'quit':
        quit()
    elif option == '1':
        n = input("Student's name: ")
    elif option == '2':

        c = input
