print("this is calculater \n to determine the area of a shape")
print("choose your shape using the numbers assigned in the list")
print("or press 0 followed by enter to exit")

def main():

    try:
        get_input = int(input('1.trapazoid\n2.circle\n3.rectangle or sqaure\n:'))
    except ValueError:
        print("!!Error: you must choose a number!!")
        return main()
        
    if get_input < 0:
        print("!!Error: Invalid entry be positive!!")
        return main()
    if get_input == 0:
        raise SystemExit("Thank You for using Area Calc Lite")
    if get_input > 3:
        print("!!Error: Please select a proper value!!")
        return main()
      
    if get_input == 1:
        base_one = int(input("Enter length of base 1: "))
        base_two = int(input("Enter length of base 2: "))
        height = int(input("Enter height: "))
    
        area_trap = ((base_one + base_two) /2) * height
    
        print("the area of your trapazoid is:", area_trap)
        return main()
    
    if get_input == 2:
        pi = 3.14159
        radius = int(input("Enter Radius: "))
        area_c = pi * (radius * radius)
        print("The area of your circle is", area_c)
        return main()
        
    if get_input == 3:
        leng = int(input("Enter Length: "))
        width = int(input("Enter Width: "))
        area_quad = leng * width
        print('the area of your quadralatteral is',area_quad)
        return main()
if __name__ == "__main__":
    main()
    
