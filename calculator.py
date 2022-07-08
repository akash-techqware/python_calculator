def addition(num1,num2):
    result=num1+num2
    print(result)
    
def substraction(num1,num2):
    result=num1-num2
    print(result)

def multiplaction(num1,num2):
    result=num1 * num2
    print(result)
    
def division(num1,num2):
    if num2 == 0.0:
        print("Divide by zero not possible")
    else:
        result=num1/num2
        print(result)
    

while True:
    # Display menu
    print("Select your desired operation from below :")
    print("1 for Addition")
    print("2 for Substracton")
    print("3 for Multiplaction")
    print("4 for Division")
    print("Press Q or q to quit !")

    # Accept user choice
    choice = input("Enter your desidred number of choice:")
    
    if choice == 'Q' or choice == 'q':
        break

    # Accept value as float
    num1 = float(input("Enter first value:"))
    num2 = float(input("Enter seconfd value:"))

    if choice == '1':
        addition(num1, num2)
    elif choice == '2':
        substraction(num1, num2)
    elif choice == '3':
        multiplaction(num1, num2)
    elif choice == '4':
        division(num1, num1)
    else:
        print("Invalid choice" )
        
    print("\n")
