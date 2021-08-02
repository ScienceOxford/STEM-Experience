import csv

# create a new dictionary to keep track of all the fruit
fruit = {}

with open('ExampleData.csv', newline='') as csvfile:
    data = csv.reader(csvfile)

    for row in data:
        if row[0].startswith('1'):
            # if this is the first time it encounters this fruit, add it to the dictionary with the number of them
            if row[1] not in fruit:
                fruit[row[1]] = int(row[2])
            # if this fruit is already in the dictionary, add this number to the total
            else:
                fruit[row[1]] = fruit[row[1]] + int(row[2])

            # the same code as above, but in one statement
            #fruit[row[1]] = fruit.get(row[1], 0) + int(row[2])
    print(fruit)
