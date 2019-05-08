from __future__ import division
import csv
from data import Semeval
import similarities as sim
import pandas as pd
from nltk.corpus import wordnet_ic
import statistics
import numpy as np


f = open('../stsbenchmark/sts-test.csv')

w = open('./out.txt', 'a')

reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)


brown_ic = wordnet_ic.ic('ic-brown.dat')
semcor_ic = wordnet_ic.ic('ic-semcor.dat')

scores = {"real" : [],
          "aguirre" : [],
          "sim_path" : [],
          "wup" : [],
          "jcn_brown" : [],
          "jcn_semcor" : [],
          "lin_brown" : [],
          "lin_semcor" : []}

data = []

for row in reader:

    if row[0] == 'main-news':
        tmp = Semeval(row[0], row[1], row[2], row[4], row[5], row[6])
        data.append(tmp)


def normalize(data, ori_min, ori_max, min, max):

    ori = ori_max - ori_min

    valueScaled = float(float(data) - ori_min) / float(ori)

    return valueScaled



def calcData(data, method):

    count = 0

    success = 0
    margin = 0.1

    for d in data:
        count +=1

        if method == 'real':
            scores[method].append(float(d.score))

        elif method == 'aguirre':
            scores[method].append(float(sim.aguirreSimilarity(d.sentence1, d.sentence2)))

        elif method == 'sim_path' or method == 'wup':
            scores[method].append(float(sim.liuWangSimilarity(d.synsets1, d.synsets2, method)))

        elif method.endswith('brown'):
            scores[method].append(float(sim.liuWangSimilarity(d.synsets1, d.synsets2, method, brown_ic)))

        elif method.endswith('semcor'):
            scores[method].append(float(sim.liuWangSimilarity(d.synsets1, d.synsets2, method, semcor_ic)))

        if method != 'real' and float(d.score) - margin < scores[method][-1] < float(d.score) + margin:
            success += 1

    return count, statistics.mean(scores[method]), success

def fillDataFrame(data, dataset, method='real'):

    count, mean, success = calcData(data, method)

    dataset['Count'].append(count)
    dataset['Mean'].append(mean)
    dataset['Success'].append(success)
    dataset['Success Perc'].append(success / count * 100.0)

    return dataset


for d in data:
    d.score = normalize(d.score, 0, 5, 0, 1)

methods = ['real', 'aguirre', 'sim_path', 'wup', 'jcn_brown', 'jcn_semcor', 'lin_brown', 'lin_semcor']

dataset = {'Method': methods,
           'Count': [],
           'Mean': [],
           'Success' : [],
           'Success Perc' : []}


for method in methods:
    dataset = fillDataFrame(data, dataset, method)

df = pd.DataFrame(dataset)

w.write(str(df[['Method', 'Count', 'Mean', 'Success', 'Success Perc']]))

w.write('\n\n CORRELATION: \n\n')

corr = []

for method in methods:
    corr.append(np.corrcoef(scores['real'], scores[method])[0, 1])
    # print ('Correlation of ' + key + ' -> ' + str(np.corrcoef(scores['real'], scores[key])[0, 1]))

dataset_2 = {'Method': methods,
           'Values': corr}

df = pd.DataFrame(dataset_2)

w.write(str(df[['Method', 'Values']]))
