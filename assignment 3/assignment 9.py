def summing_numbers(list_1, list_2):

    new_list = list(map(lambda num1, num2: int(num1) + int(num2), list_1, list_2))
    return new_list
    



if __name__ == "__main__" :

    while True:
        try:
            list1 = input("Enter your numbers for list 1 separated by space:\t").split()
            list2 = input("Enter your numbers for list 2 separated by space:\t").split()

            sum = summing_numbers(list1, list2)
        except ValueError:
            print("try again with numbers")
            continue
        if len(list1) != len(list2):
            print("Try again")
            continue
        print(sum)
        break

    