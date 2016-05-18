import csv

with open('bugs list - Sheet1 - ex.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Priority'] == 'critical':
            row['Priority'] = 'high'

writer = csv.writer(open('output6.csv', 'w'))
writer.writerows(row)