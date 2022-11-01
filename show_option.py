def print_operation():


def isContinued(str):
    
    while True:
        next_calculation = input("Let's do next calculation? (yes/no): ").lower()
        if next_calculation == "no":
            re = input("Are you sure? (yes/no): ").lower()  # re-check
            if re == "yes":
                return False
            elif re == "no":
                return True
        elif next_calculation == "yes":
            return True
        else:   # yes/no가 아닌 다른 대답이 입력된 경우
            print("Please answer yes or no.")

        


                

