#----- Shape Printer (MEDIUM) -----#

running = True
while running:
    print("1. Half-Triangle")
    print("2. Rectangle")
    print("3. Line")
    shape = input("What shape do you want to draw? ")
    if shape == 'quit':
        quit()
    elif shape != '1' and shape != '2' and shape != '3':
        quit()
    
    if shape == '1': #half-triangle
        height = int(input("Height of triangle: "))
        line = ""
        print("")
        for i in range(0, height):
            for star in range(0, 1):
                line += "* "
            print(line)
    
    elif shape == '2': #rectangle
        width = int(input("Width: "))
        height = int(input("Height: "))
        line = ""
        print("")
        for w in range(0, width):
            line += "* "
        for h in range(0, height):
            print(line)
    
    elif shape == '3': #line
        direct = input("Horizontal (h) or Vertical (v)? ")
        len = int(input("Length: "))
        print("")
        if direct == 'h': #horizontal
            line = ""
            for i in range(0, len):
                line += "* "
            print(line)
        elif direct == 'v': #vertical
            for i in range(0, len):
                print("*")
        else:
            print("Invalid Input")
            continue
    else:
        print("Invalid Input")
        continue

    print("")