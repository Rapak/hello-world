import xml.etree.cElementTree as etree

parser = etree.XMLParser(encoding="utf-8")
targetTree = etree.parse( 'habraharb_all.txt', parser=parser )
root = targetTree.getroot()
each_elem = []
for child in root.iter('item'):
 items = {}
 categ = []
 for item in child:
   if item.tag == 'title':
    items['title'] = item.text
   if item.tag == 'author':
    items['author'] = item.text
   for category in item.iter('category'):
    categ.append(category.text)
    items['category'] = categ
    each_elem.append(items)
print each_elem