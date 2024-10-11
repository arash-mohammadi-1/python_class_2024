my_file = open("classes\class 11.py",'w')
my_file.write("I LOVE PIZZA")

my_file
data_text = my_file.read()
#data_text = my_file.read(2)

print(data_text)
my_file.close()