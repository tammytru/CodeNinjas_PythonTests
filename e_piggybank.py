#----- PIGGY BANK (EASY) -----#
accFlag = 1
while accFlag == 1:
    acct = str(input("Enter 10 digit account number: "))
    if len(acct) != 10:
        print("Invalid account number")
    elif not acct.isnumeric():
        print("Invalid account number")
    else:
        accFlag = 0

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