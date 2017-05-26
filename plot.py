import matplotlib.pyplot as plt
import csv

with open('eggs.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            print ', '.join(row)


plt.plot([1,2,3,4], [1,4,9,16])
plt.axis([0, 6, 0, 20])
plt.show()
