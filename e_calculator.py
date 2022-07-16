#----- Calculator (EASY) -----#

while True:
    print("Type 'quit' at anytime to exit calculator.")
    num1 = input("Enter the first number: ")
    if num1 == 'quit':
        quit()
    sign = input("Calculation (+ - / *): ")
    if sign == 'quit':
        quit()
    num2 = input("Enter the second number: ")
    if num2 == 'quit':
        quit()

    num1 = float(num1)
    num2 = float(num2)
    if sign == '+':
        ans = num1 + num2
    elif sign == '-':
        ans = num1 - num2
    elif sign == '/':
        ans = num1 / num2
    elif sign == '*':
        ans = num1 * num2
    else:
        print("Invalid Input. Try Again")
        continue
    
    print("Answer:", ans)

