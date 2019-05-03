from nltk.corpus import stopwords
from nltk import word_tokenize

class Data:

    #Some contractions with multiple expansions have been deleted for simplicity purposes
    contractions = {
        "ain't": "am not",
        "aren't": "are not",
        "can't": "cannot",
        "can't've": "cannot have",
        "'cause": "because",
        "could've": "could have",
        "couldn't": "could not",
        "couldn't've": "could not have",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "hadn't": "had not",
        "hadn't've": "had not have",
        "hasn't": "has not",
        "haven't": "have not",
        "he'd've": "he would have",
        "how'd": "how did",
        "how'd'y": "how do you",
        "how'll": "how will",
        "I'd've": "I would have",
        "I'm": "I am",
        "I've": "I have",
        "isn't": "is not",
        "it'd've": "it would have",
        "let's": "let us",
        "ma'am": "madam",
        "mayn't": "may not",
        "might've": "might have",
        "mightn't": "might not",
        "mightn't've": "might not have",
        "must've": "must have",
        "mustn't": "must not",
        "mustn't've": "must not have",
        "needn't": "need not",
        "needn't've": "need not have",
        "o'clock": "of the clock",
        "oughtn't": "ought not",
        "oughtn't've": "ought not have",
        "shan't": "shall not",
        "sha'n't": "shall not",
        "shan't've": "shall not have",
        "she'd've": "she would have",
        "should've": "should have",
        "shouldn't": "should not",
        "shouldn't've": "should not have",
        "so've": "so have",
        "that'd've": "that would have",
        "there'd've": "there would have",
        "they'd've": "they would have",
        "they're": "they are",
        "they've": "they have",
        "to've": "to have",
        "wasn't": "was not",
        "we'd've": "we would have",
        "we'll": "we will",
        "we'll've": "we will have",
        "we're": "we are",
        "we've": "we have",
        "weren't": "were not",
        "what're": "what are",
        "what've": "what have",
        "when've": "when have",
        "where'd": "where did",
        "where've": "where have",
        "who've": "who have",
        "why've": "why have",
        "will've": "will have",
        "won't": "will not",
        "won't've": "will not have",
        "would've": "would have",
        "wouldn't": "would not",
        "wouldn't've": "would not have",
        "y'all": "you all",
        "y'all'd": "you all would",
        "y'all'd've": "you all would have",
        "y'all're": "you all are",
        "y'all've": "you all have",
        "you'd've": "you would have",
        "you're": "you are",
        "you've": "you have"
    }

    punctuationMarks = ['\'',
                        '"',
                        '\\',
                        '/',
                        ',',
                        ':',
                        '.',
                        ':',
                        '-',
                        '_',
                        '?',
                        '!',
                        '*',
                        '(',
                        ')']

    def __init__(self, genre, subset, year, score, sentence1, sentence2):

        self.genre = genre
        self.subset = subset
        self.year = year
        self.score = score

        self.sentence1 = []
        self.sentence2 = []

        #Process text before introducing it on the lists

        self.sentence1 = self.processText(sentence1)
        self.sentence2 = self.processText(sentence2)



    def processText(self, sentence):

        #All lowercase
        sentence = sentence.lower()

        #Tokenize
        tmp = word_tokenize(sentence)

        #Delete stopwords
        stop_words =set(stopwords.words('english'))

        words = []

        for w in tmp:
            if w not in stop_words:
                words.append(w)

        words = self.deletePunctuation(words)

        return words

    def deletePunctuation(self, inputWords):

        words = []

        for word in inputWords:
            # Remove contractions
            if word in self.contractions:
                words.append(self.contractions[word])
            # Remove punctuation marks
            elif word in self.punctuationMarks:
                continue
            else:
                words.append(word)

        return words
