def try_rercreation(number):

    if number == 1 or number == 2 :
        return 1 

    elif number > 2:
        result = try_rercreation(number - 1) + try_rercreation(number - 2)
        return (result)
    
    else :
        result = 0

if __name__ == "__main__":
    while True:
        try :
            times = int(input('enter how meny times:')) 
            result = try_rercreation(times)
            print (result)
            break
        except ValueError :
            print ("enter only numbers")
            continue
        