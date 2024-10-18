import csv

with open("samples_for_assignment\employees.csv","r", encoding= "utf=8") as csv_file :
    reader = csv.reader(csv_file)

    headers = next(reader)
    print(headers)

    for row in reader:
        print(row)