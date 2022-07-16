#----- CALENDAR (HARD) -----#

class Event:
    def __init__(self, t, m, d, y):
        self.title = t
        self.month = m
        self.day = d
        self.year = y

    def change_title(self, t):
        self.title = t

    def change_date(self, m, d, y):
        self.month = m
        self.day = d
        self.year = y

    def print(self):
        print("Title:", self.title)
        print("Date:", self.month, int(self.day), int(self.year))

def print_calendar():
    print("------------------")
    for i in range(0, len(events)):
        print("Event", i+1)
        events[i].print()
        print()
    print("------------------")

events = []

while True:
    print("1. Add new event")
    print("2. Print entire calendar")
    print("3. Delete an event")
    i = input("Choose an option: ")

    if i == 'quit':
        quit()

    elif i == '1':
        t = input("Title: ").lower()
        m = input("Month (ex. jan): ").lower()
        while len(m) != 3:
            print("Invalid month. Try again.")
            m = input("Month (ex. jan): ").lower()
        d = int(input("Day: "))
        while d < 0 or d > 31:
            print("Invalid day. Try again.")
            d = int(input("Day: "))
        y = int(input("Year (ex. 2022): "))
        while y < 1000 or y > 9999:
            print("Invalid year. Try again.")
            y = int(input("Year (ex. 2022): "))
        events.append(Event(t, m, d, y))

    elif i == '2':
        print_calendar()

    elif i == '3':
        print_calendar()
        i = int(input("What event do you want to change? "))
        i -= 1
        if i < 0 or i > len(events):
            print("Invalid event. Try again")
            continue
        
        e = events[i]
        option = input("Change title (t) or date (d): ")
        if option == 't':
            n = input("New title: ")
            e.change_title(n)
        elif option == 'd':
            m = input("Month (ex. jan): ").lower()
            while len(m) != 3:
                print("Invalid month. Try again.")
                m = input("Month (ex. jan): ").lower()
            d = int(input("Day: "))
            while d < 0 or d > 31:
                print("Invalid day. Try again.")
                d = int(input("Day: "))
            y = int(input("Year (ex. 2022): "))
            while y < 1000 or y > 9999:
                print("Invalid year. Try again.")
                y = int(input("Year (ex. 2022): "))
            e.change_date(m, d, y)

    elif i == '4':
        print_calendar()
        i = int(input("What event number would you like to delete? "))
        i -= 1
        if i < 0 or i > len(events):
            print("Invalid event. Try again")
            continue
        del events[i]

    else:
        print("That is not an option. Try again")