import csv
from data import Semeval
import similarities as sim

f = open('../stsbenchmark/sts-test.csv')

reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)


data = []

for row in reader:

    tmp = Semeval(row[0], row[1], row[2], row[4], row[5], row[6])
    data.append(tmp)


sentence1 = data[1].sentence1
sentence2 = data[1].sentence2

synsets1 = data[1].synsets1
synsets2 = data[1].synsets2

print(sentence1)

print(sentence2)

aguirre = sim.aguirreSimilarity(sentence1, sentence2)

print (aguirre)

sim.liuWangSimilarity(synsets1, synsets2)


