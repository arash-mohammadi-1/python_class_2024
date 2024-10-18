# numpy is one of the bigest laibrery take a look👍
import xml.etree.ElementTree as ET

tree = ET.parse("samples_for_assignment\\books.xml")

root = tree.getroot()

print(root.tag)

#for grand_child in root :
#    for child in grand_child:
#        print(child.tag)
#        print(child.attrib)
#        print(10 * "-")

for book in root.findall("book") :
#   print(book.tag)
    print(book.find("title").text)
    print(book.find("author").text)
    print(book.find("price").text)
    print(10 * "_")