#----- TO-DO LIST (MEDIUM) -----#

def printList(list):
    print("----------------------")
    print("Number of items:", len(list))
    for i in range(0, len(list)):
        print(i+1, ":", list[i])
    print("----------------------")

todo = []
finished = []

while True:
    print("1. Print to-do list")
    print("2. Add to-do")
    print("3. Check off to-do")
    print("4. Print completed list")
    user = input("What would you want to do? ")

    if user == 'quit':
        quit()
    elif user == '1':
        printList(todo)
    elif user == '2':
        item = input("New to-do: ")
        todo.append(item)
    elif user == '3':
        printList(todo)
        print("What item would you like to check-off?")
        item = input("Enter the item number: ")
        item = int(item) - 1
        if item < 0 or item > len(todo):
            print("Invalid item. Try again")
            continue
        finished.append(todo[item])
        todo.pop(item)
    elif user == '4':
        printList(finished)
    else:
        print("Invalid option. Try again")
