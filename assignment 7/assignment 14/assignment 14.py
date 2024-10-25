import csv

with open("assignment 7\\assignment 14\sample_file.csv", "r", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)

    headers = next(reader)
    print(headers)

    amount_index = headers.index("Amount")
    
    sum_amount = 0 

    for row in reader:
        print(row)
      
        sum_amount += float(row[amount_index])

    print("Total Amount:", sum_amount)
