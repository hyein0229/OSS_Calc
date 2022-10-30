# Program make a simple calculator

import calc_function as cf
import show_option as opt

opt.print_operation()

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", cf.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", cf.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", cf.multiply(num1, num2))

        elif choice == '4':
                result = cf.divide(num1, num2)
                if result != None:
                    print(num1, "/", num2, "=", cf.divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no

        continued = True
        while True:
            next_calculation = input("Let's do next calculation? (yes/no): ")
            result = opt.isContinued(next_calculation)
            if result != None:   
                if result == False: 
                    continued = False
                break
            else:   # yes/no가 아닌 다른 대답이 입력된 경우
                print("Please answer yes or no.")
        if continued == False:
            break


    else:
        print("Invalid Input")

