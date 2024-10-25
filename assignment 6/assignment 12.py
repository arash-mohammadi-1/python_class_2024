import json

with open("assignment 6\info_company.json","r",encoding="utf8") as file :
    data = json.load(file)
    if "sector" in data :
        sector = data["sector"] 

    if "fullTimeEmployees" in data :
        fullTimeEmployees = data["fullTimeEmployees"]

    if "longBusinessSummary" in data:
        long_business_summary = data["longBusinessSummary"]
        long_business_summary = long_business_summary.replace(".","\n")
    

    if "city" in data :
        city = data["city"] 

    if "phone" in data :
       phone_company =  data["phone"] 

with open("assignment 6\\report_of_the_company.txt", "w", encoding="utf8") as file:
    file.write(" ")

with open("assignment 6\\report_of_the_company.txt", "a", encoding="utf8") as file:
    file.write("\nhello and welcome to our company\ntoday I will tell you more about our company.")
    file.write(f"\nthis is all the sector our company has :{sector}.")
    file.write(f"\nwe have over {fullTimeEmployees} fullTimeEmployees.")
    file.write(f"\nthis is our longBusinessSummary \n{long_business_summary}.\n")
    file.write(f"\nwe are in {city} city.")
    file.write(f"\nif you wanted to call us this is our number {phone_company}.")