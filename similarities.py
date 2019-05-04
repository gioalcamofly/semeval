from nltk.corpus import wordnet as wn



#Word similarity

def getMaxSimilarityPath(word, S):

    score = 0.0

    for synset in S:
        tmp = word.path_similarity(synset)
        if tmp > score:
            score = tmp

    return score

def getPathSimilarity(synsets1, synsets2):

    for word1 in synsets1:
        for word2 in synsets2:
            print(str(word1) + ' and ' + str(word2) + ' = ' + str(word1.path_similarity(word2)))




#Sentence similarity

def aguirreSimilarity(sentence1, sentence2):

    aligned = 0
    for word in sentence1:
        if word in sentence2:
            aligned += 1

    return (2*aligned)/(len(sentence1) + len(sentence2))


def liuWangSimilarity(synsets1, synsets2):

    T = union(synsets1, synsets2)

    print(T)

    V1 = calculateVector(T, synsets1)

    print(V1)




# Auxiliar methods

def union(sentence1, sentence2):

    return list(set(sentence1) | set(sentence2))

def calculateVector(T, S):

    V = []

    for word in T:

        if word in S:
            V.append(1.0)
        else:
            V.append(getMaxSimilarityPath(word, S))

    return V