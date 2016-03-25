
import xml.etree.ElementTree as ET
import pyPdf

tocount = pyPdf.PdfFileReader(open('/home/nikhil/Desktop/example.pdf'))
count_of_pages=tocount.getNumPages()

tree = ET.parse('/home/nikhil/Desktop/testing.xml')

container = tree.find("page")
#print container

newlinelist=[]


data = []
for elem in container:

    if(elem.tag=="text"):
        key=int(elem.attrib['top'])

        print key


        data.append((key, elem))


data.sort()  #sorting the tags basing on top value

# insert the last item from each tuple
container[:] = [item[-1] for item in data]

tree.write("/home/nikhil/Desktop/new-data1.xml")  #rewriting the sorted values to new xml file

#preprocessing :--

'''
for elem in container:

    if(elem.tag=="text"):

        newline = elem
        newline.attrib["top"]

        newline.set("bootom",1)
        newlinelist.append(newline)
        print newlinelist


'''





























