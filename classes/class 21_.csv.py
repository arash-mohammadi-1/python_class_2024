import csv

csv_input_path = "samples_for_assignment\employees.csv"
with open(csv_input_path,"r", encoding= "utf=8") as csv_file :
    reader = csv.reader(csv_file)

    headers = next(reader)
    print(headers)

    for row in reader:
        print(row)



csv_output_path = "samples_for_assignment\out.csv"

fields = ["Name", "Family", "Age", "Score"]
rows = [
    ["Arash", "mohammadi", "15", "0"],
    ["Taha", "hokmabadi", "15", "0"],
    ["Alireza", "Yazdani", "16", "0"],
    ["setayesh", "shojae", "14", "0"], 
    ["sogand", "jangi", "14", "0"],
    ["Niayesh", "Adaszabe", "13", "0"],
    ["mohammadhossin", "yaghoubiezade", "13", "0"],
    ["Amieali", "Niazmand", "14", "0"],
    ["Alireza", "mohammadi", "15", "0"],
]

with open(csv_output_path, "w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(fields)
    for row in rows:
        csv_writer.writerow(row)