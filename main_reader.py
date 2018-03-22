import csv

with open('part_1.csv','r') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        print(", ".join(row))

print(data[1])

