def try_rercreation(number):
    if number > 0:
        result = number + try_rercreation(number - 1)
        print (result)
    else :
        result = 0

    return result

if __name__ == "__main__":
    try_rercreation(10)