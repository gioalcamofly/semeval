import csv
from data import Data

f = open('../stsbenchmark/sts-test.csv')

reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)


data = []

for row in reader:

    tmp = Data(row[0], row[1], row[2], row[4], row[5], row[5])
    data.append(tmp)


print(data[5].sentence2)

