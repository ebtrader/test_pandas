import csv

with open('top150.csv') as i:
    reader = csv.reader(i)
    your_list = list(reader)

x = your_list
print(x)
