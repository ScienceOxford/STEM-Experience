import csv

# create a new variable to keep track of the oranges
total_oranges = 0

with open('ExampleData.csv', newline='') as csvfile:
    data = csv.reader(csvfile)

    # for every row, print it (if it starts with '1' and has 'oranges' as the next column)
    for row in data:
        if row[0].startswith('1') and row[1] == 'oranges':
            print(row[2])
            # add the number of oranges to the total
            #total_oranges = total_oranges + int(row[2])

    # print the final total number of oranges
    #print(total_oranges)
