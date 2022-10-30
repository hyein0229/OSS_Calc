def print_operation():
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

def isContinued(str):
    lower_str = string.lower(str)
    if lower_str == "no":
        reply = string.lower(input("Are you sure? (yes/no): ")
        if reply == "yes":
            return False
        elif reply == "no":
            return True
        else:
            reply = string.lower(input("Please answer yes or no. Let's do next calculation? (yes/no): ")
            return isContinued(reply)
    elif lower_str == "yes":
        return True
    else:
        reply = string.lower(input("Please answer yes or no. Let's do next calculation? (yes/no): ")
        return isContinued(reply)

        


                

