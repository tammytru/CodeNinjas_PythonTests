#----- PIGGY BANK (EASY) -----#

total = 0

while True:
    print("1. Deposit")
    print("2. Withdrawl")
    print("3. Check Funds")
    print("type 'q' to quit")
    task = input("What would you like to do? ")

    if task == '1':
        amount = input("Deposit amount: ")
        total += float(amount)
        print("BALANCE: $", total)
    elif task == '2':
        amount = float(input("Withdrawl amount: "))
        if amount > total:
            print("Error! Insufficient Funds")
        else:
            total -= amount
            print("BALANCE: $", total)
    elif task == '3':
        print("BALANCE: $", total)
    elif task == 'q':
        quit()
    else:
        print("Invalid Input. Try Again")
    
    print("---------------------")