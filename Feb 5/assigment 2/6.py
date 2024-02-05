# 6.Reading the data inside the xml file to a variable under the name data
import xml.etree.ElementTree as ET

tree = ET.parse('Feb 5/assigment 2/5.xml')
root = tree.getroot()

data = ET.tostring(root, encoding='utf8').decode('utf8')
print(data)