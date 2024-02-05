# 5.Reading Data From an XML File
# i-Finding Tags 
import xml.etree.ElementTree as ET

tree = ET.parse('Feb 5/assigment 2/5.xml')
root = tree.getroot()

tags = [elem.tag for elem in root.iter()]

# ii - Extracting from tags
print(tags)


data = {}
for elem in root.iter():
    if elem.text:
        data[elem.tag] = elem.text

# Print data
print("\nData:")
for tag, value in data.items():
    print(f"{tag}: {value}")