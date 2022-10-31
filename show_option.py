def print_operation():
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

def isContinued(str):
    lower_str = str.lower()
    if lower_str == "no":
        str2 = input("Are you sure? (yes/no): ")  # re-check
        lower_str2 = str2.lower()
        if lower_str2 == "yes":
            return False
        elif lower_str2 == "no":
            return True
    elif lower_str == "yes":
        return True
    return None

        


                

