vorodi = int(input("enter your numbers:"))
vorodi = list (vorodi)

def tavan_two(enters) :
    return enters ** 2

resalt = map(tavan_two,vorodi)
print(list(resalt))