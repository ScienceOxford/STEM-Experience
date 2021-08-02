# import the csv library
import csv

# open the file as a csv and read it
with open('ExampleData.csv', newline='') as csvfile:
    data = csv.reader(csvfile)

    # for every row, print it (if it starts with '1')
    for row in data:
        #if row[0].startswith('1'):
            print(row)
