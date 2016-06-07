from lxml import etree

course_xml = etree.parse('course.txt')
xslt = etree.parse('transform.txt')
transform = etree.XSLT(xslt)
result = transform(course_xml)
print(etree.tostring(result, pretty_print=True))