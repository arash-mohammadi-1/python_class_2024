import json 

#این مشکل داره بخاطره ورودی که داره
with open("assignment 5\map_book.txt", "r") as file :
    data = json.load(file)

for key, value in data.items():
    print(key)
    print(10 * "_")
    print(value)
    print(10 * "#")