print ("salam be bazi hads khosh amadid\ndar in bazi shoma bayad be adadi ke man beheah fkr makonal ra hads bezani")
import random
number = random.randint(1,100)
while True :
    user_number = input ("lotfan adad ra vared konid :")
    try:
        user_number = int(user_number)
    except ValueError:
   
   
        print("lotfan adad vared konid")
    if user_number < number :
        print ('bozorg tareh')
    elif user_number > number :
        print ('kochik tareh')
    if user_number == number :
        print ("afarin drost hads zadi👍")
        break
