def print_operation():

def isContinued(str):
    lower_str = str.lower()
    if lower_str == "no":
        reply = input("Are you sure? (yes/no): ")
        lower_reply = reply.lower()
        if lower_reply == "yes":
            return False
        elif lower_reply == "no":
            return True
        else:
            reply = input("Please answer yes or no. Let's do next calculation? (yes/no): ")
            return isContinued(reply)
    elif lower_str == "yes":
        return True
    else:
        reply = input("Please answer yes or no. Let's do next calculation? (yes/no): ")
        return isContinued(reply)

        


                

