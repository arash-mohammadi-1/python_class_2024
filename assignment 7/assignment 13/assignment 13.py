import xml.etree.ElementTree as shop_list
link = input("enter your link:")
tree = shop_list.parse(link)

root = tree.getroot()

for task in root.findall("Task") :

    print(task.find("Title").text)
    print(task.find("DueDate").text)
    print(task.find("Priority").text)
    print(task.find("Status").text)
    print(10 * "_")