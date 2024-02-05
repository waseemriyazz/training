# 7.Writing XML Files

import xml.etree.ElementTree as ET

tree = ET.parse('Feb 5/assigment 2/7.xml')
root = tree.getroot()

new_root = ET.Element('root7')
new_element = ET.SubElement(new_root, 'child7')
new_element.text = 'ye childwa 7 ka hai'

new_tree = ET.ElementTree(new_root)
new_tree.write('Feb 5/assigment 2/7.xml')
