from nltk.corpus import wordnet_ic
from scipy import spatial



#Word similarity

def getMaxSimilarityPath(word, S):

    score = 0.0

    for synset in S:
        tmp = word.path_similarity(synset)
        if tmp > score:
            score = tmp

    return score

def getMaxSimilarityWup(word, S):

    score = 0.0

    for synset in S:
        tmp = word.wup_similarity(synset)
        if tmp > score:
            score = tmp

    return score

def getMaxSimilarityJcn(word, S):

    score = 0.0
    ic = wordnet_ic.ic('ic-brown.dat')

    for synset in S:
        try:
            tmp = word.jcn_similarity(synset, ic)
        except:
            tmp = 0.0
        if tmp > score:
            score = tmp

    return score

def getMaxSimilarityLin(word, S):

    score = 0.0
    ic = wordnet_ic.ic('ic-brown.dat')

    for synset in S:
        try:
            tmp = word.lin_similarity(synset, ic)
        except:
            tmp = 0.0
        if tmp > score:
            score = tmp

    return score

#Sentence similarity

def aguirreSimilarity(sentence1, sentence2):

    aligned = 0.0
    for word in sentence1:
        if word in sentence2:
            aligned += 1.0

    return (2*aligned)/(len(sentence1) + len(sentence2))


def liuWangSimilarity(synsets1, synsets2):

    T = union(synsets1, synsets2)

    print(T)

    V1 = calculateVector(T, synsets1)
    V2 = calculateVector(T, synsets2)

    similarity = 1 - spatial.distance.cosine(V1, V2)


    print(V1)

    print(V2)

    print(str(similarity))




# Auxiliar methods

def union(sentence1, sentence2):

    return list(set(sentence1) | set(sentence2))

def calculateVector(T, S):

    V = []

    for word in T:

        if word in S:
            V.append(1.0)
        else:
            V.append(getMaxSimilarityWup(word, S))

    return V