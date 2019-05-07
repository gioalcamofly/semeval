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

    try:
        return (2*aligned)/(len(sentence1) + len(sentence2))
    except:
        return 0.0


def liuWangSimilarity(synsets1, synsets2, method):

    T = union(synsets1, synsets2)

    V1 = calculateVector(T, synsets1, method)
    V2 = calculateVector(T, synsets2, method)

    similarity = 1 - spatial.distance.cosine(V1, V2)


    return similarity




# Auxiliar methods

def union(sentence1, sentence2):

    return list(set(sentence1) | set(sentence2))

def calculateVector(T, S, method):

    V = []

    for word in T:

        try:
            if word in S:
                V.append(1.0)
            elif method == 'sim_path':
                V.append(getMaxSimilarityPath(word, S))
            elif method == 'wup':
                V.append(getMaxSimilarityWup(word, S))
        except:
            V.append(0.0)

    return V