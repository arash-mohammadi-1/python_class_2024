age = (input('please intur your age: '))
try :
    age = int(age)
    if age >= 18 :
        print ('you can vote')
    else:
        print ("you cant vote")
except ValueError:
    print("lotfan adad vared konid")
except Exception :
    print('thier is an ERORR')