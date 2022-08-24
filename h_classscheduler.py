#----- CLASS SCHEDULER (HARD) -----#

class Student:
    def __init__(self, n):
        self.name = n
        self.sched = []
    
    def add_class(self, clas):
        self.sched.append(clas)
    
    def drop_class(self, i):
        self.sched.remove(i)

    def check_class(self, clas):
        if clas in self.sched:
            return True
        else:
            return False

    def print_sched(self):
        print("Student:", self.name)
        for i in range(0, len(self.sched)):
            print(i+1, ":", self.sched[i])

def print_students():
    print("------------------")
    for i in range(0, len(students)):
        print("Student", i+1)
        students[i].print_sched()
        print()
    print("------------------")

students = []

while True:
    print("1. Add new student")
    print("2. Edit schedule")
    print("3. Remove student")
    print("4. Print all students")
    option = input("Choose an option: ")

    if option == 'quit':
        quit()
    elif option == '1':
        n = input("Student's name: ")
        students.append(Student(n))
    elif option == '2':
        print_students()
        print("Which student's schedule would you like to EDIT?")
        i = int(input("Enter student number: "))
        i -= 1
        if i < 0 or i > len(students):
            print("Invalid student. Try again")
            continue
        
        s = students[i]
        choice = '1'
        while choice != 'done':
            print("Add (a) or Remove (b) a class?")
            choice = input("Type 'done' to return to main menu: ")
            if choice.lower() == 'a':
                cl = input("Class name: ")
                s.add_class(cl)
            elif choice.lower() == "b":
                cl = input("Class name: ").lower()
                if s.check_class(cl):
                    s.drop_class(cl)
                else:
                    print("Student is not yet enrolled in that class.")
            else:
                print("That is not an option. Try again.")
    elif option == '3':
        print_students()
        i = int(input("Which student would you like to REMOVE? "))
        i -= 1
        if i >= 0 and i < len(students):
            print("Student", i+1, "has been deleted.")
            del students[i]
        else:
            print("Invalid student. Try again")
    elif option == '4':
        print_students()
    else:
        print("That is not an option.")
