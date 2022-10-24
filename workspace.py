import csv

pod = 'LPOTL'
name = 'JackSlack'
link = 'jackdotcom'
new = (name + ',' + link)

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('pods.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',', escapechar=' ',quoting=csv.QUOTE_NONE)

        for line in csv_reader:
            csv_writer.writerow(line)

        csv_writer = csv_writer.writerow([new])

    # with open('pods.csv', 'a', newline='') as new_pod:
    #     csv_writer = csv_writer.writerow(new)

csv_dict = {}

f = open('pods.csv', 'r')
dict_reader = csv.reader(f)

for row in dict_reader:
    csv_dict[row[0]] = row[1]

print(csv_dict)