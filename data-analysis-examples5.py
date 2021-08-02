import csv
import matplotlib.pyplot as plt

const = {}

with open('GaN2020.csv', newline='') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        if row[len(row)-1].startswith('United States'):
            const[row[len(row)-4]] = const.get(row[len(row)-4], 0) + 1
            #print(row)
    print(const)

plt.pie(const.values(), labels=const.keys(), autopct='%1.0f%%')
#plt.plot(const.keys(), const.values(), color="blue")
plt.show()
