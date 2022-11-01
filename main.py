# Program make a simple calculator

import calc_function as cf
import show_option as opt
import logging

def set_file_logger(logger_name, file_name, level):

    logger = logging.getLogger(logger_name)

    if level == 1:
        logger.setLevel(logging.INFO)
    elif level == 2:
        logger.setLevel(logging.ERROR)

    log_format = logging.Formatter(fmt = "%(asctime)s - %(levelname)s : %(message)s")

    file_handler = logging.FileHandler(filename = file_name)
    file_handler.setFormatter(log_format)

    logger.addHandler(file_handler)

    return logger


logger1 = set_file_logger("normal roution logger", "calc.log", 1)  # 정상 루틴 로거
logger2 = set_file_logger("Abnormal roution logger", "error.log", 2)  # 비정상 루틴 로거

console = logging.StreamHandler()
logger1.addHandler(console)

opt.print_operation()

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            logger1.info(str(num1) + " + " + str(num2) +  " = " + str(cf.add(num1, num2)))

        elif choice == '2':
            logger1.info(str(num1) + " - " + str(num2) +  " = " + str(cf.subtract(num1, num2)))

        elif choice == '3':
            logger1.info(str(num1) +  " * " +  str(num2) +  " = " +  str(cf.multiply(num1, num2)))

        elif choice == '4':
                result = cf.divide(num1, num2)
                if result == None:
                    logger2.error("divide by zero error")
                else:
                    logger1.info(str(num1) +  " / " + str(num2) + " = " + str(result))

        # check if user wants another calculation
        # break the while loop if answer is no
        if(opt.isContinued() == False):
            break

    else:
        print("Invalid Input")
        logger2.error("Input is out of range(1,2,3,4)")

