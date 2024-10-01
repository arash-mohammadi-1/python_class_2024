
#my first try
# i am a professional
# do not mess with me
# name = tuple[input("enter your name:")]
# last_name = tuple[input("enter yout last name:")]

# full_name = list(zip(name , last_name))
# print (list[full_name])
while True:
    try:
        number_of_tuples = int(input("HOW many tuples do you want:"))
        break
    except ValueError:
        print("try again for the love of jesus.")
    except KeyboardInterrupt:
        print("\nYou have found the easter egg of this program!\nNow die!\nDeleting OS...")
        number_of_tuples = 0
        while True:
            print("HA", end="")

list_of_tuples = []


count = 0
while count < number_of_tuples :
    
    try:
        enters = input("enter tuple like this (a b): ")
        a, b = map(int, enters.split())
        list_of_tuples.append((a, b))
        count = count + 1
    except ValueError:
        print("try again for the love of jesus.")
    except KeyboardInterrupt:
        print("HAHAHAHA")        
reault = sorted(list_of_tuples, key=lambda x: x [1])
print(reault)
