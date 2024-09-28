try :
    times = int(input('enter how meny times:')) 
except ValueError :
    print ("enter only numbers")

def try_rercreation(number):

    if number == 1 or number == 2 :
        return 1 

    elif number > 0:
        result = try_rercreation(number - 1) + try_rercreation(number - 2)
        print (result)
    
    else :
        result = 0

    return result

if __name__ == "__main__":
    try :
        times = int(input('enter how meny times:')) 
    except ValueError :
        print ("enter only numbers")

    try_rercreation(times)