def tavan_two(numbers) :
    power_of_two = list(map(lambda x: x ** 2 , numbers))
    return power_of_two

if __name__ == "__main__":
    while True:
        try:
            number_list = list(map(int, input("enter your numbers separated by space: ").split()))
            break
        except ValueError:
            print("Try again you dumb blitch")
            continue
    print(tavan_two(number_list))