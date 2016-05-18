from datetime import datetime
s1 = '11 Jan 2016'
s1 = datetime.strptime(s1, '%d %b %Y')
print s1
s2 = '4 April 2011'
s2 = datetime.strptime(s2, '%w %B %Y')
print s2
s3 = '11.03.2014'
s3 = datetime.strptime(s3, '%d.%m.%Y')
print s3
s4 = '03/24/91'
s4 = datetime.strptime(s4, '%m/%d/%y')
print s4