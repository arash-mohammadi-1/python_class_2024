numbers = (list(input("enter your number with spaces:").split()))
try :
    def only_even(numbers):
        for number in numbers:
            if int(number) % 2 == 0:
                return True
            else :
                return False 
except ValueError :
    print("try again with numbers")

result = filter(only_even, numbers)
print(list(result))
