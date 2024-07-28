import xml.dom.minidom
# parse the XML file
xml_doc = xml.dom.minidom.parse('tours.xml')
# get the root element
root = xml_doc.documentElement
print('Root is',root)

# get all the package elements
packages = xml_doc.getElementsByTagName('package')
# loop through the packages and extract the data
for package in packages:
    package_id = package.getAttribute('id')
    description =   package.getElementsByTagName('description')[0].childNodes[0].data
    price = package.getElementsByTagName('price')[0].childNodes[0].data
    duration = package.getElementsByTagName('duration')[0].childNodes[0].data
    print('Package ID:', package_id)
    print('Description:', description)
    print('Price:', price)