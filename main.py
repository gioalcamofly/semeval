from __future__ import division
import csv
from data import Semeval
import similarities as sim
import pandas as pd


f = open('../stsbenchmark/sts-test.csv')

w = open('./out.txt', 'w')

reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)


data = []

for row in reader:

    tmp = Semeval(row[0], row[1], row[2], row[4], row[5], row[6])
    data.append(tmp)


# sentence1 = data[1].sentence1
# sentence2 = data[1].sentence2
#
# synsets1 = data[1].synsets1
# synsets2 = data[1].synsets2
#
# print(sentence1)
#
# print(sentence2)
#
# aguirre = sim.aguirreSimilarity(sentence1, sentence2)
#
# print (aguirre)
#
# sim.liuWangSimilarity(synsets1, synsets2)
#

# for x in data:
#     aguirre = sim.aguirreSimilarity(x.sentence1, x.sentence2)
#
#     w.write("Sentence 1: " + ' '.join(x.sentence1) + " | Sentence 2: " + ' '.join(x.sentence2) + " -> " + str(aguirre) + "\n")

def normalize(data, ori_min, ori_max, min, max):

    ori = ori_max - ori_min
    obj = max - min

    valueScaled = float(float(data) - ori_min) / float(ori)

    return valueScaled



def calcData(data, method):

    count = 0
    mean = 0.0

    success = 0
    margin = 0.1

    for d in data:
        count +=1

        if method == 'real':
            mean += float(d.score)

        elif method == 'aguirre':
            aguirre = sim.aguirreSimilarity(d.sentence1, d.sentence2)
            if float(d.score) - margin < aguirre < float(d.score) + margin:
                success += 1
            mean += aguirre

        elif method == 'sim_path':
            sim_path = sim.liuWangSimilarity(d.synsets1, d.synsets2, method)
            if float(d.score) - margin < sim_path < float(d.score) + margin:
                success += 1
            mean += sim_path

        elif method == 'wup':
            sim_path = sim.liuWangSimilarity(d.synsets1, d.synsets2, method)
            if float(d.score) - margin < sim_path < float(d.score) + margin:
                success += 1
            mean += sim_path

    return count, mean/count, success

def fillDataFrame(data, dataset, method='real'):

    count, mean, success = calcData(data, method)

    dataset['Count'].append(count)
    dataset['Mean'].append(mean)
    dataset['Success'].append(success)
    dataset['Success Perc'].append(success / count * 100.0)

    return dataset


for d in data:
    d.score = normalize(d.score, 0, 5, 0, 1)

methods = ['real', 'aguirre', 'sim_path', 'wup']

dataset = {'Method': methods,
           'Count': [],
           'Mean': [],
           'Success' : [],
           'Success Perc' : []}


for method in methods:
    dataset = fillDataFrame(data, dataset, method)

df = pd.DataFrame(dataset)

print(df[['Method', 'Count', 'Mean', 'Success', 'Success Perc']])



