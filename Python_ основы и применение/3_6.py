from xml.etree import ElementTree
tree = ElementTree.parse('example.xml')
root = tree.getroot()

blaise = root[0]


cert = blaise[2]
cert.set('type','with distinction')
tree.write('example_copy.xml')
print(blaise[2].attrib)