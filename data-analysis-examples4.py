import csv
# import part of the matplotlib library
import matplotlib.pyplot as plt

fruit = {}

with open('ExampleData.csv', newline='') as csvfile:
    data = csv.reader(csvfile)

    for row in data:
        if row[0].startswith('1'):
            fruit[row[1]] = fruit.get(row[1], 0) + float(row[2])#*float(row[3][2:])

    print(fruit)

# create a pie chart from the dictionary values, with the keys as labels
plt.pie(fruit.values(), labels=fruit.keys(), autopct='%1.0f%%')
plt.show()
