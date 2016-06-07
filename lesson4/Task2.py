import json

with open("bugs.json") as json_file:
    json_data = json.load(json_file)

    data = []
    for row in json_data:
        row['Owner'] = 'qa5'
        data.append(row)
    print data

with open('bugs_new.txt', 'w') as outfile:
    json.dump(data, outfile, sort_keys=True,indent=4)