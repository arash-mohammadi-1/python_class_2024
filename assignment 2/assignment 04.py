print("hello che mikhahy")


kharj_dict = {}


def add_kala (kala, mablagh):
    mablagh = float(mablagh)
    if kala in kharj_dict:
        mablagh += float(kharj_dict[kala])
    else :
        kharj_dict [add_kala] = mablagh
    

def total_mablagh () :
    total = 0
    for key in kharj_dict :
       total +=  float(kharj_dict[key])
    return total


def set_budget():
    while True:
        budget = input("cheghadr pol dary ?🧐 ")
        try:
            budget = float(budget)
            return budget
        except ValueError:
            print("try again (only numbers)")


def total_sum () :
    sum = float(total_mablagh())
    leftovers = budget - sum
    return leftovers


while True:
    print (f"1. add new kharj\n2. show sum of kharj\n3. set budget\n4. show sum of budget\n5. exit program")
    barnameh =  input("enter you chosen platform: ")

    
    if barnameh == "1":
        kala = input ('what is your kala name?\t')
        while True :
            mablagh = input ("how much is your kala worth?\t")
            if mablagh.isdigit() is False :
                print ("try again (only numbers)")
                continue
            break
        add_kala(kala, mablagh)
        print("successful!")
        continue

    if barnameh == "2": 
        sum = total_mablagh()
        print (f'your total kharj is {sum}')
        continue

    if barnameh == "3":
        budget = set_budget()
        print(f"your badget is now{budget}")

    if barnameh == "4":
    
        summ = total_sum()
        print (f'your total budget is {summ}')
        continue
 
    if barnameh == "5":
       print ("gameover😢")
       break
    else :
        print ("try again. choose from 1,2,3,4,5")
    