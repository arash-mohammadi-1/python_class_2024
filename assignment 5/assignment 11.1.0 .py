book_link = input("enter your book link:")
count = input("What word do you want me to count for you?:")

with open(book_link, 'r', encoding= "utf-8") as file:
    contents = file.read()
    
    file.seek(0) 
    splited_lines = len(file.readlines())

    splited_word = len(contents.split())

    counted_file = contents.count(count)

    print(contents)

with open("assignment 5\\report.txt", "w",encoding= "utf-8") as report:
    report.write(" ")
    
with open("assignment 5\\report.txt", "a",encoding= "utf-8") as report:
    report.write("\n"f"The count of the lines that this book has: {splited_lines}""\n")
    report.write(f"The count of the word you gave me: {counted_file}""\n")
    report.write(f"The count of all words: {splited_word}""\n")


with open("assignment 5\\report.txt", "r",encoding= "utf-8") as report:
    report = report.read()
    print(report)
