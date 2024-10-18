import json

sector_input = input("what sector do you work for?")

try :
        fullTimeEmployees_input = input("who many fullTimeEmployees do the company have?")
except ValueError :
     print("pleaes enter only numbers")

longBusinessSummary_input = input("tell us about your longBusinessSummary:")

city_input = input("where is the cpompany from(only put in the city that company is on):")

try:
    phone_number = input("what is thew company phone number(enter your number with ___ like : 0999_456_9999)?")
except ValueError :
     print("pleaes enter only numbers")
     
with open("assignment 6\info_company.json","r",encoding="utf8") as file :
    data = json.load(file)
    if "sector" in data :
        data["sector"] = sector_input

    if "fullTimeEmployees" in data :
        data["fullTimeEmployees"] = fullTimeEmployees_input

    if "longBusinessSummary" in data :
        data["longBusinessSummary"] = longBusinessSummary_input

    if "city" in data :
        data["city"] = city_input

    if "phone" in data :
        data["phone"] = phone_number

with open("assignment 6/info_company.json", "w", encoding="utf8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)



